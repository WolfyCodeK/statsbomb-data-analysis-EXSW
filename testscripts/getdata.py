#test script for getting player data freom image
from roboflow import Roboflow
import json

rf = Roboflow(api_key="rqtpvnIQ9hZvR3ql6tzC")
project = rf.workspace().project("fyp-amjew")
model = project.version(4).model

# infer on a local image
data = model.predict("testscripts\main.png", confidence=40, overlap=30).json()

with open("testscripts/predictioncoords.json", "w") as json_file:
    json.dump(data, json_file)


input_image="testscripts\main.png"
output_image="testscripts\prediction.jpg"
# visualize your prediction
model.predict(input_image, confidence=40, overlap=30).save(output_image)

'''

Pitch data
Width - 67.75m
length - 104.8m
6 yard box - 18m wide
centre circle - 18m wide



'''