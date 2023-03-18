import vtkplotlib as vpl
from stl.mesh import Mesh

halfron = "rendertest\halfron.stl"
stadium = "rendertest\EuroArena.stl"

# Read the STL using numpy-stl
mesh = Mesh.from_file(halfron)
stadium = Mesh.from_file(stadium)


# Plot the mesh
vpl.mesh_plot(mesh)
vpl.mesh_plot(stadium)

# Show the figure
vpl.view(camera_position=[0,0,10])
vpl.show()