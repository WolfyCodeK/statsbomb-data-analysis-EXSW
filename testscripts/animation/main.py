import bpy

# Clear the existing mesh objects in the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Import the OBJ file
obj_file_path = "testscripts/render/output.obj"
bpy.ops.import_scene.obj(filepath=obj_file_path)

# Assume you have a list of coordinates for the object to move to
coordinates = [
    (10000, 110000, 110000),
    (210000, 210000, 210000),
    (310000, 310000, 310000),
    (410000, 410000, 410000),
]

# Select the object you want to animate
obj = bpy.context.selected_objects[0]

# Set the animation duration and frame rate
duration = 100  # Animation duration in frames
frame_rate = 24  # Frame rate of the animation

# Set keyframes for each coordinate
for i, coord in enumerate(coordinates):
    frame_number = int(i * duration / (len(coordinates) - 1))
    obj.location = coord
    obj.keyframe_insert(data_path="location", frame=frame_number)

# Set the scene's end frame
bpy.context.scene.frame_end = duration


gltf_file_path = "testscripts/animation/output.gltf"
bpy.ops.export_scene.gltf(filepath=gltf_file_path, check_existing=False)
