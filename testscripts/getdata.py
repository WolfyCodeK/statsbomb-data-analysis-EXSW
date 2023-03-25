#test script for getting player data freom image
from roboflow import Roboflow
rf = Roboflow(api_key="rqtpvnIQ9hZvR3ql6tzC")
project = rf.workspace().project("football-players-detection-3zvbc")
model = project.version(2).model

# infer on a local image
print(model.predict("testscripts\main.png", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("testscripts\main.png", confidence=40, overlap=30).save("testscripts\prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())