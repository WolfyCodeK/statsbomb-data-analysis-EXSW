import bpy
outputloc="testscripts/render/pitch.fbx"
playermodelloc="models\halfron.obj"
pitchloc="models\Soccer Field With Field Texture Big.fbx"

# Import the FBX file
bpy.ops.import_scene.fbx(filepath=pitchloc)

# Get a reference to the imported object
obj = bpy.context.selected_objects[0]

# Export the object as an OBJ file with material and texture files
bpy.ops.export_scene.obj(filepath=outputloc, check_existing=False, use_materials=True, use_triangles=True)

# Delete the imported object
bpy.data.objects.remove(obj)

# Delete the imported materials
for material in bpy.data.materials:
    if material.users == 0:
        bpy.data.materials.remove(material)

# Delete the imported textures
for texture in bpy.data.textures:
    if texture.users == 0:
        bpy.data.textures.remove(texture)
