import json
import time
import bpy
import math
import xml.etree.ElementTree as ET
import ast

def default_rotate(obj):
    angle = math.radians(-90)
    axis = 'X'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

def rotatehometeam(obj):
    angle = math.radians(90)
    axis = 'Z'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

def rotateawayteam(obj):
    angle = math.radians(-90)
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

def makeobject(*obj_name):
    # Load the halfron.obj file
    bpy.ops.import_scene.obj(filepath=playermodelloc)

    # Get a reference to the object
    obj_name = bpy.context.selected_objects[0]

    # Set the object's location to 0,0,0
    obj_name.location = (0, 0, 0)
    default_rotate(obj_name)
    return obj_name

def makeball(*obj_name):
    # Load the ball.obj file
    bpy.ops.import_scene.obj(filepath=ballloc)

    # Get a reference to the object
    obj_name = bpy.context.selected_objects[0]

    # Set the object's location to 0,0,0
    
    obj_name.scale = (15000, 15000, 15000)
    obj_name.location = (33000 *ballpos[1][0],33000 *ballpos[1][1],(33000 *ballpos[1][2]))


    default_rotate(obj_name)
    return obj_name

def setcoords(obj,coordinates):
    obj.location = (33000 * coordinates[0],33000 * coordinates[1],33000 * coordinates[2])
    return obj


outputloc = "testscripts/render/output.obj"
mtlloc = "testscripts/render/output.mtl"
playermodelloc = "models/halfron.obj"
ballloc = "models/Ball/Ball.obj"
pitchloc = "models/Soccer Field With Field Texture Big.fbx"
matchdata="C:/Users/harve/Downloads/MCI Women's Files/g2312135_SecondSpectrum_tracking-produced.xml"
teamlineuploc="C:/Users/harve/Downloads/MCI Women's Files/g2312135_SecondSpectrum_meta.json"

def get_player_locations(matchdata=matchdata, input_time=0.0):
    root = ET.parse(matchdata).getroot()
    player_locations = []

    for frame in root.iter('frame'):
        if float(frame.get('time')) == input_time:
            for player in frame:
                if player.tag == 'player':
                    id = player.get('id')
                    loc = player.get('loc')
                elif player.tag == 'ball':
                    id = 'ball'
                    loc = player.get('loc')
                    global ballpos 
                    ballpos = [id,ast.literal_eval(loc)]
                player_locations.append([id, loc])
            break

    return player_locations

objs_to_render=[]

def createallplayers(teams):
    player_locations = get_player_locations(matchdata,input_time=0.0)
    for element in player_locations:
        if element[0] != "ball":
            print(element)
            #home team
            if any(element[0] in sublist for sublist in teams[0]):
                print("home team")
                temp_obj = makeobject()
                temp_obj = rotatehometeam(temp_obj)
                temp_obj = change_material_color_to_blue(temp_obj)
                temp_obj = setcoords(temp_obj,ast.literal_eval(element[1]))
                objs_to_render.append(temp_obj)
            if any(element[0] in sublist for sublist in teams[1]):
                print("away team")
                temp_obj = makeobject()
                temp_obj = rotateawayteam(temp_obj)
                temp_obj = change_material_color_to_red(temp_obj)
                temp_obj = setcoords(temp_obj,ast.literal_eval(element[1]))
                objs_to_render.append(temp_obj)

def export_objects_to_obj(objs_to_render, outputloc):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the objects in the list
    for obj in objs_to_render:
        obj.select_set(True)

    # Export the selected objects as a single OBJ file
    bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_selection=True)

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

teams = getteamplayerlist()
createallplayers(teams)
ball = makeball()          
objs_to_render.append(ball)
print(objs_to_render)
export_objects_to_obj(objs_to_render, outputloc)