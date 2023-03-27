import bpy
import math

def default_rotate(obj):
    angle = math.radians(-90)
    axis = 'X'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

outputloc="testscripts/render/output.obj"
playermodelloc="models\halfron.obj"
pitchloc="models\Soccer Field With Field Texture Big.fbx"

# Load the halfron.obj file
bpy.ops.import_scene.obj(filepath=playermodelloc)

# Get a reference to the object
obj = bpy.context.selected_objects[0]

# Set the object's location to 0,0,0
obj.location = (0, 0, 0)
default_rotate(obj)

# Export the scene as an OBJ file
bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_selection=True)

