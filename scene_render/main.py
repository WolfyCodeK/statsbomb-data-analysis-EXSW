import vtkplotlib as vpl
from stl.mesh import Mesh

halfron = "scene_render\halfron.stl"
stadium_stl = "scene_render\EuroArena.stl"
textures_dir = "scene_render\Textures"

# Read the STL using numpy-stl
mesh = Mesh.from_file(halfron)
stadium = Mesh.from_file(stadium_stl)

# Plot the mesh
vpl.mesh_plot(mesh)
vpl.mesh_plot(stadium)

# Show the figure
vpl.view(camera_position=[0,1,0],up_view=[0,1,0])
vpl.show()