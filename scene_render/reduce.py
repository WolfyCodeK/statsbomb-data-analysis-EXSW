import meshlib.mrmeshpy as mr

# load high-resolution mesh:
mesh = mr.loadMesh(mr.Path("path of OG file .stl"))

# decimate it with max possible deviation 0.5:
settings = mr.DecimateSettings()
settings.maxError = 0.5
result = mr.decimateMesh(mesh, settings)
print(result.facesDeleted)
# 708298
print(result.vertsDeleted)
# 354149

# save low-resolution mesh:
mr.saveMesh(mesh, mr.Path("path of output .stl "))