import bpy

def main(timedata,playercoords):
    # Clear the existing mesh objects in the scene
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Import the OBJ file
    obj_file_path = "testscripts/render/output.obj"
    bpy.ops.import_scene.obj(filepath=obj_file_path)

    # example coords
    coordinates = [
        (10000, 110000, 110000),
        (210000, 210000, 210000),
        (310000, 310000, 310000),
        (410000, 410000, 410000),
    ]

    # Set the animation duration and frame rate, make this depend on length    
    frame_rate = 24  # Frame rate of the animation
    duration = int(100*frame_rate/(timedata[2]-timedata[0]))  # Animation duration in frames
    #total seconds in fr/duration

    scalefactor = 47500

    for i in range(22):
        print(i)
        # Select the object you want to animate
        obj = bpy.context.selected_objects[i]

        coordinates=playercoords[i]

        for data in playercoords[i]:
            coordinates.append([data[0]*scalefactor,data[1]*scalefactor,data[2]*scalefactor])

        # Set keyframes for each coordinate
        for i, coord in enumerate(coordinates):
            frame_number = int(i * duration / (len(coordinates) - 1))
            obj.location = coord
            obj.keyframe_insert(data_path="location", frame=frame_number)

    # dont forget ball
    ball_obj = bpy.context.selected_objects[22]

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

    for json_str in json_list:
        result = json.loads(json_str)
        #print(f"result: {result}")
        #print(isinstance(result, dict))
    
    print(f"result: {len(result['homePlayers'])}")
    player_coords=[]
    return


if __name__ == '__main__':
    timedata=[0,1,20]
    playercoords= player_coords(timedata)
    main(timedata,playercoords)
    
