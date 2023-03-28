import bpy
import math
import xml.etree.ElementTree as ET
import ast

# Create a new material
blue_material = bpy.data.materials.new(name="BlueMaterial")

# Set the material's base color to blue
blue_material.use_nodes = True
bsdf_node = blue_material.node_tree.nodes.get("Principled BSDF")
if bsdf_node is not None:
    bsdf_node.inputs["Base Color"].default_value = (0, 0, 1, 1)  # (R, G, B, Alpha)

def assign_material(obj, material):
    if len(obj.data.materials) == 0:
        obj.data.materials.append(material)
    else:
        obj.data.materials[0] = material

def default_rotate(obj):
    angle = math.radians(-90)
    axis = 'X'
    obj.rotation_euler.rotate_axis(axis, angle)
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

def setcoords(obj,coordinates):
    obj.location = (33000 * coordinates[0],33000 * coordinates[1],33000 * coordinates[2])
    return obj

outputloc = "testscripts/render/blue/blue.obj"
mtlloc = "testscripts/render/blue/blue.mtl"
playermodelloc = "models/halfron.obj"
pitchloc = "models/Soccer Field With Field Texture Big.fbx"
matchdata="C:/Users/harve/Downloads/MCI Women's Files/g2312135_SecondSpectrum_tracking-produced.xml"

def get_player_locations(matchdata=matchdata, input_time=0.04):
    root = ET.parse(matchdata).getroot()
    player_locations = []

    for frame in root.iter('frame'):
        if float(frame.get('time')) == input_time:
            for player in frame:
                if player.tag == 'player':
                    num = player.get('num')
                    loc = player.get('loc')
                elif player.tag == 'ball':
                    num = 'ball'
                    loc = player.get('loc')
                player_locations.append([num, loc])
            break

    return player_locations

objs_to_render=[]

def createallplayers():
    player_locations = get_player_locations(matchdata,input_time=0.04)
    for element in player_locations:
        if element[0] != "ball":
            temp_obj = makeobject()
            temp_obj = setcoords(temp_obj,ast.literal_eval(element[1]))
            # Assign the blue material to the object
            assign_material(temp_obj, blue_material)
            objs_to_render.append(temp_obj)

def export_objects_to_obj(objs_to_render, outputloc):
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the objects in the list
    for obj in objs_to_render:
        obj.select_set(True)

    # Export the selected objects as a single OBJ file
    bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_selection=True)

createallplayers()
print(objs_to_render)
export_objects_to_obj(objs_to_render, outputloc)
