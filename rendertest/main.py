import vtkplotlib as vpl
from stl.mesh import Mesh

halfron = "rendertest\halfron.stl"
stadium_stl = "rendertest\EuroArena.stl"
textures_dir = "rendertest\Textures"

# Read the STL using numpy-stl
mesh = Mesh.from_file(halfron)
stadium = Mesh.from_file(stadium_stl)

# Plot the mesh
vpl.mesh_plot(mesh)
vpl.mesh_plot(stadium)

# Show the figure
vpl.view(camera_position=[0,1,0])
vpl.show()