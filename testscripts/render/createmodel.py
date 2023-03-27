import bpy
import math
# Load the halfron.obj file
bpy.ops.import_scene.obj(filepath="models\halfron.obj")

# Get a reference to the object
obj = bpy.context.selected_objects[0]

# Set the object's location to 0,0,0
obj.location = (0, 0, 0)
dup_obj = obj.copy()

#rotate
# Rotate the object by 45 degrees around the Z-axis
angle = math.radians(-90)
axis = 'X'
obj.rotation_euler.rotate_axis(axis, angle)

# Create a duplicate of the object
bpy.context.scene.collection.objects.link(dup_obj)

# Set the duplicate object's location to 1,1,1
dup_obj.location = (10000, 10000, 1)

# Select both objects
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
dup_obj.select_set(True)

# Export the scene as an OBJ file
bpy.ops.export_scene.obj(filepath="output.obj", check_existing=False, use_selection=True)
