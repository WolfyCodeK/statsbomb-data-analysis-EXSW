import bpy

def main(timedata, playercoords):
    # Clear the existing mesh objects in the scene
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Import the OBJ file
    obj_file_path = "MCI/mancity/pitch/models/output.obj"
    bpy.ops.import_scene.obj(filepath=obj_file_path)

    # Set the animation duration and frame rate
    frame_rate = 25  # Frame rate of the animation
    duration = int((frame_rate*(timedata[2] - timedata[0])))  # Animation duration in frames

    scalefactor = 20000

    for i in range(23):
        frameCoords = playercoords[i]

        currentCoords = []
        ballSelected = False
        
        for player in frameCoords:
            playerID = str(player[1])
            #print(playerID + " ~ " + str(player[0]))  
            
            for j in range(23):
                selectedObj = bpy.context.selected_objects[j]
                objName = str(selectedObj.name)
                objName, sep, tail = objName.partition('_Object')
                
                if playerID == objName:
                    currentCoords = player[0]
                    break;
                
        # get ball
        if currentCoords == []:
            selectedObj = bpy.context.selected_objects[22]
            currentCoords = frameCoords[0]
            ballSelected = True
                                    
        selectedObj.location = [currentCoords[0],currentCoords[1],currentCoords[2]]

        if ballSelected == False: 
            # Scale the player coordinates
            scaled_coordinates = [
                [((coord[0][0] * scalefactor)), ((coord[0][1] * scalefactor)), coord[0][2]]
                for coord in frameCoords
            ]
        else: 
            # Scale the ball coordinates
            scaled_coordinates = [
                [coord[0] * 37500, coord[1] * 37500, coord[2]]
                for coord in frameCoords
            ]

        #scaled_coordinates.insert(0,[currentCoords[0],currentCoords[1],currentCoords[2]])

        # Set keyframes for each coordinate
        for j, coord in enumerate(scaled_coordinates):
            frame_number = int(j * duration / (len(scaled_coordinates) - 1))
            selectedObj.location = coord
            selectedObj.keyframe_insert(data_path="location", frame=frame_number)
            if (i == 0):
                print(selectedObj.name + str(coord))
            
    # Set the scene's end frame
    bpy.context.scene.frame_end = duration
    gltf_file_path = "testscripts/animation/output.gltf"
    bpy.ops.export_scene.gltf(filepath=gltf_file_path, check_existing=False)



'''
take in match time seconds and period for start and end [start seconds, period, endtime seconds, period]
create the players
add keyframe movements here
add animations


'''
import json,time

def player_coords(timedata):
    #return player coords, list of lists of lists
    gamefile="largefiles/g2312135_SecondSpectrum_tracking-produced.jsonl"
    with open(gamefile, 'r') as json_file:
        json_list = list(json_file)

    # vid is at 25 fps
    time_to_prod = (timedata[2]-timedata[0])*25

    #first half
    firsthalflist,secondhalflist=[],[]
    if timedata[1] == 1:
        for json_str in json_list:
            result = json.loads(json_str)
            tmp_list=[]
            if result['period'] == 1:
                for element in result['homePlayers']:
                    tmp_list.append((element['xyz'], element['playerId']))
                for element in result['awayPlayers']:
                    tmp_list.append((element['xyz'], element['playerId']))
                tmp_list.append(result['ball']['xyz'])
                firsthalflist.append(tmp_list)
        ffhalfdata=[[] for x in range(23)]
        for element in firsthalflist:
            for i in range(len(element)):
                ffhalfdata[i].append(element[i])
        first_half_final=[]
        for data in ffhalfdata:
            first_half_final.append(data[:time_to_prod])
        print("first half data created")
        return first_half_final

    # second half
    if timedata[1] == 2:
        for json_str in json_list:
            result = json.loads(json_str)
            tmp_list=[]
            if result['period'] == 2:
                for element in result['homePlayers']:
                    tmp_list.append((element['xyz'], element['playerId']))
                for element in result['awayPlayers']:
                    tmp_list.append((element['xyz'], element['playerId']))
                tmp_list.append(result['ball']['xyz'])
                secondhalflist.append(tmp_list)
        fshalfdata=[[] for x in range(23)]
        for element in secondhalflist:
            for i in range(len(element)):
                fshalfdata[i].append(element[i])  
        second_half_final=[]
        for data in fshalfdata:
            second_half_final.append(data[:time_to_prod])  
        print("second half data created")
        return second_half_final
    
    


if __name__ == '__main__':
    timedata=[0,1,20]
    playercoords= player_coords(timedata)
    main(timedata,playercoords)
    
