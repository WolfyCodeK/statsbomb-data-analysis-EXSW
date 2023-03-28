import bpy
import math

def default_rotate(obj):
    angle = math.radians(-90)
    axis = 'X'
    obj.rotation_euler.rotate_axis(axis, angle)
    return obj

outputloc = "testscripts/render/output.obj"
mtlloc = "testscripts/render/output.mtl"
playermodelloc = "models/halfron.obj"
pitchloc = "models/Soccer Field With Field Texture Big.fbx"

# Load the halfron.obj file
bpy.ops.import_scene.obj(filepath=playermodelloc)

# Get a reference to the object
obj = bpy.context.selected_objects[0]

# Set the object's location to 0,0,0
obj.location = (0, 0, 0)
default_rotate(obj)

# Assign a blue material to the object
mat = bpy.data.materials.new(name="Blue")
mat.diffuse_color = (0, 0, 1, 1)  # Set the alpha value to 1 for opaque material
obj.data.materials.append(mat)

# Create a duplicate of the object
dup_obj = obj.copy()
bpy.context.scene.collection.objects.link(dup_obj)

# Set the duplicate object's location to 1,1,1
dup_obj.location = (30000,30000,1)

# Assign a red material to the duplicate object
mat = bpy.data.materials.new(name="Red")
mat.diffuse_color = (1, 0, 0, 1)  # Set the alpha value to 1 for opaque material
dup_obj.data.materials.append(mat)

# Export the scene as an OBJ file with material properties
bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_selection=True, use_materials=True)

# Export the material properties as an MTL file
with open(mtlloc, 'w') as mtl_file:
    for mat in bpy.data.materials:
        mtl_file.write("newmtl " + mat.name + "\n")
        mtl_file.write("Kd " + str(mat.diffuse_color[0]) + " " + str(mat.diffuse_color[1]) + " " + str(mat.diffuse_color[2]) + "\n")
        mtl_file.write("\n")
