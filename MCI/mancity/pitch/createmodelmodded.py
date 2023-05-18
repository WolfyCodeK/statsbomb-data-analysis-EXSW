import json
import os
import time
import zipfile
import bpy
import math
import xml.etree.ElementTree as ET
import ast
from datetime import datetime
import gltf


def default_rotate(obj):
    angle = math.radians(-90)
    axis = 'X'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

def rotatehometeam(obj, newAngle):
    angle = math.radians(newAngle)
    axis = 'Z'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

def rotateawayteam(obj, newAngle):
    angle = math.radians(newAngle)
    axis = 'Z'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

def change_material_color_to_blue(obj):
    # Ensure the object has a material slot
    if not obj.material_slots:
        mat = bpy.data.materials.new(name="New Material")
        obj.data.materials.append(mat)
    else:
        mat = obj.material_slots[0].material

    # Set the material color to blue
    mat.use_nodes = True
    bsdf_node = mat.node_tree.nodes.get('Principled BSDF')
    if bsdf_node:
        bsdf_node.inputs['Base Color'].default_value = (0, 0, 1, 1)

    return obj

def change_material_color_to_red(obj):
    # Ensure the object has a material slot
    if not obj.material_slots:
        mat = bpy.data.materials.new(name="New Material")
        obj.data.materials.append(mat)
    else:
        mat = obj.material_slots[0].material

    # Set the material color to red
    mat.use_nodes = True
    bsdf_node = mat.node_tree.nodes.get('Principled BSDF')
    if bsdf_node:
        bsdf_node.inputs['Base Color'].default_value = (1, 0, 0, 1)

    return obj

def makeobject(obj_name):
    # Load the halfron.obj file
    bpy.ops.import_scene.obj(filepath=playermodelloc)

    # Get a reference to the object
    obj = bpy.context.selected_objects[0]

    # Set the object's name
    obj.name = str(obj_name)

    # Set the object's location to 0,0,0
    obj.location = (0, 0, 0)
    default_rotate(obj)
    return obj

global scalefactor
scalefactor = 47500

def makeball(*obj_name):
    # Load the ball.obj file
    bpy.ops.import_scene.obj(filepath=ballloc)

    # Get a reference to the object
    obj_name = bpy.context.selected_objects[0]

    # Set the object's location to 0,0,0
    
    obj_name.scale = (15000, 15000, 15000)
    obj_name.location = (scalefactor *ballpos[1][0],scalefactor *ballpos[1][1],(scalefactor *ballpos[1][2]))


    default_rotate(obj_name)
    return obj_name

def setcoords(obj,coordinates):
    obj.location = (scalefactor * coordinates[0],scalefactor * coordinates[1],coordinates[2])
    return obj

#change that to specify per new model time
outputloc = "../../../MCI/mancity/pitch/models/output.obj"
mtlloc = "../../../MCI/mancity/pitch/models/output.mtl"
outputlocglb = "../../../MCI/mancity/pitch/glbmodels/output.glb"
playermodelloc = "../../../models/halfron.obj"
texturesfolder= "models/Textures"
ballloc = "../../../models/Ball/Ball.obj"
matchdata="../../../largefiles/g2312135_SecondSpectrum_tracking-produced.xml"
teamlineuploc="../../../largefiles/g2312135_SecondSpectrum_meta.json"
pitchloc="../../../models/euro-arena-soccer-stadium-euro-2020/source/Models/EuroArena.obj"

def add_pitch_obj(pitchloc):
    # Import the OBJ file
    bpy.ops.import_scene.obj(filepath=pitchloc)

    # Get a reference to the imported object(s)
    imported_objects = bpy.context.selected_objects

    scale_factor = 20000

    for obj in imported_objects:
        
        obj.scale *= scale_factor
        angle = math.radians(-90)
        axis = 'Y'
        obj.rotation_euler.rotate_axis(axis, angle)

    return imported_objects

#this bits slow
def get_player_locations(matchdata, input_time,matchPeriod):
    root = ET.parse(matchdata).getroot()
    player_locations = []
    print(input_time)
    time.sleep(5)

    for period in root.iter('period'):
        if period.get('number') == str(matchPeriod):
            for frame in period.iter('frame'):
                if float(frame.get('time')) == input_time:
                    for player in frame:
                        if player.tag == 'player':
                            id = player.get('id')
                            loc = player.get('loc')
                        elif player.tag == 'ball':
                            id = 'ball'
                            loc = player.get('loc')
                            global ballpos 
                            ballpos = [id, ast.literal_eval(loc)]
                            print("aaaaa")
                            print(ballpos)
                        player_locations.append([id, loc])
                    break
    return player_locations

objs_to_render=[]

def createallplayers(teams,total_seconds,matchPeriod):

    # Get location of players 1 second before
    if (total_seconds > 0):
        player_previous_locations = get_player_locations(matchdata,total_seconds - 1,matchPeriod)
    
    if total_seconds == 0:
        player_previous_locations = get_player_locations(matchdata,total_seconds,matchPeriod)
        
    player_locations = get_player_locations(matchdata,total_seconds,matchPeriod)
    
    
    for i in range(len(player_locations)):
        element = player_locations[i]
        if element[0] != "ball":
            #home team
            if any(element[0] in sublist for sublist in teams[0]):
                print("home team")
                temp_obj = makeobject(element[0])
                angle = getPlayerAngle(
                    ast.literal_eval(element[1]), 
                    ast.literal_eval(player_previous_locations[i][1])
                )
                
                 # Default angle value
                if (angle == None):
                    angle = 90
                
                temp_obj = rotatehometeam(temp_obj, angle)
                print(str(i) + " ~ " + str(angle))
                temp_obj = change_material_color_to_blue(temp_obj)
                temp_obj = setcoords(temp_obj,ast.literal_eval(element[1]))
                objs_to_render.append(temp_obj)
            if any(element[0] in sublist for sublist in teams[1]):
                print("away team")
                temp_obj = makeobject(element[0])
                angle = getPlayerAngle(
                    ast.literal_eval(element[1]), 
                    ast.literal_eval(player_previous_locations[i][1])
                )
                
                # Default angle value
                if (angle == None):
                    angle = -90
                
                temp_obj = rotateawayteam(temp_obj, angle)
                temp_obj = change_material_color_to_red(temp_obj)
                temp_obj = setcoords(temp_obj,ast.literal_eval(element[1]))
                objs_to_render.append(temp_obj)

def getPlayerAngle(current_location, previous_location):
    # current player coords
    xCurrent = float(current_location[0])
    yCurrent = float(current_location[1])
    
    # previous player coords
    xPrevious = float(previous_location[0])
    yPrevious = float(previous_location[1])
    
    # absoulte change in player position
    xChange = xCurrent - xPrevious
    yChange = yCurrent - yPrevious
    
    angle = None
    
    # yChange = opp, xChange = adj, tan(theta) = opp / adj 
    if (xChange != 0) and (yChange != 0):
        tanTheta = abs(yChange) / abs(xChange)
        theta = math.degrees(math.atan(tanTheta))
        
        if (xChange > 0) and (yChange > 0):
            angleCorrection = 90
        if (xChange > 0) and (yChange < 0):
            angleCorrection = 0
        if (xChange < 0) and (yChange > 0):
            angleCorrection = 180
        if (xChange < 0) and (yChange < 0):
            angleCorrection = 270  
        
        angle = theta + angleCorrection
    
    return angle

def export_objects_to_obj(objs_to_render, outputloc):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the objects in the list
    for obj in objs_to_render:
        obj.select_set(True)

    # Export the selected objects as a single OBJ file
    bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_selection=True, use_materials=True)

def export_objects_to_glb(objs_to_render, outputlocglb,total_seconds,matchperiod):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    outputlocglb = "../../../MCI/mancity/pitch/glbmodels/output.glb"
    outputname=f"../../../MCI/mancity/pitch/glbmodels/{matchperiod}_{total_seconds}.glb"

    # Select the objects in the list
    for obj in objs_to_render:
        obj.select_set(True)

    # Export the selected objects as a single glb file
    bpy.ops.export_scene.gltf(filepath=outputname, check_existing=False, use_selection=True, export_format='GLB')


with open(teamlineuploc, 'r') as file:
    json_data = json.load(file)

def get_home_players(json_data=json_data):
    home_players_data = json_data["homePlayers"]
    home_players = []

    for player in home_players_data:
        player_id = player["ssiId"]
        player_name = player["name"]
        home_players.append([player_id,player_name])

    return home_players

def get_away_players(json_data=json_data):
    away_players_data = json_data.get("awayPlayers", [])
    away_players = []

    for player in away_players_data:
        player_id = player.get("ssiId")
        player_name = player.get("name")
        away_players.append([player_id,player_name])

    return away_players

def getteamplayerlist():
    home_players = get_home_players()
    away_players = get_away_players()
    return [home_players,away_players]

def modify_obj_file(obj_file_path, mtl_file_name):

    keep_colours(mtl_file_name)

    '''
    # Read the contents of the OBJ file
    with open(obj_file_path, 'r') as f:
        lines = f.readlines()

    # Modify the third line to include the MTL file name
    lines[2] = "mtllib " + "theonethatworks.mtl" + "\n"

    # Save the modified contents back to the OBJ file
    with open(obj_file_path, 'w') as f:
        f.writelines(lines)
    '''

def keep_colours(obj_files_path):
    with open(obj_files_path, 'r') as f:
        lines = f.readlines()

    # Find the line with "newmtl Material.001"
    for i, line in enumerate(lines):
        if line.startswith("newmtl Material.001"):
            break

    # Remove all lines after the "newmtl Material.001" line
    lines = lines[:i]

    # Append selection.txt to the end of the original file
    with open("../../../MCI/mancity/pitch/models/selection.txt", "r") as f:
        selection_lines = f.readlines()
    lines += selection_lines

    # Write the modified lines back to the original file
    with open(obj_files_path, "w") as f:
        f.writelines(lines)


def zip_files():
    zip_filename = "output_files.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:

        #change these two
        # Add the output.obj file
        output_obj_file = outputloc
        zipf.write(output_obj_file, "output.obj")

        # Add the output.mtl file
        output_mtl_file = "models/output.mtl"
        zipf.write(output_mtl_file, "output.mtl")

        # Add the textures folder
        textures_folder = texturesfolder
        for folder, subfolders, filenames in os.walk(textures_folder):
            for filename in filenames:
                file_path = os.path.join(folder, filename)
                arcname = os.path.join("Textures", os.path.relpath(file_path, textures_folder))
                zipf.write(file_path, arcname)

def run_script(total_seconds,matchPeriod):
    startTime = datetime.now()
    teams = getteamplayerlist()

    createallplayers(teams,total_seconds,matchPeriod)

    ball = makeball()          
    objs_to_render.append(ball)

    # Add the pitch to the scene
    pitch_obj_loc = pitchloc
    pitch_objects = add_pitch_obj(pitch_obj_loc)
    objs_to_render.extend(pitch_objects)

    # Set the default camera position
    bpy.context.scene.camera.location = (0, 0, 10)
    bpy.context.scene.camera.rotation_euler = (0, 0, 0)

    #export_objects_to_obj(objs_to_render, outputloc)
    export_objects_to_glb(objs_to_render, outputlocglb,total_seconds,matchPeriod)
    #modify_obj_file("../../../MCI/mancity/pitch/models/output.obj", "../../../MCI/mancity/pitch/models/output.mtl")
    #zip_files()

    print(datetime.now() - startTime)
    print("to run")
    return True


import sys
import re

if __name__ == '__main__':
    #this is the time of the event
    render_time = sys.argv[1]
    print(render_time,"rendertime")
    time.sleep(10)

    pattern = r"(\d+):(\d+)"
    matchTime = re.match(pattern, render_time)
    
    matchPeriod = str(re.findall(r'[^- ]+$', render_time))
    matchPeriod = matchPeriod.removeprefix("['")
    matchPeriod = matchPeriod.removesuffix("']") 
    
    if matchTime:
        minutes = int(matchTime.group(1))
        seconds = int(matchTime.group(2))
        total_seconds = minutes * 60 + seconds

    if (int(matchPeriod) == 2):
        total_seconds -= (45 * 60)

    # Do something with the arguments
    run_script(total_seconds,matchPeriod)

