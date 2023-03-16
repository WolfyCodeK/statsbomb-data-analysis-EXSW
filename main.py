from jsonController import *

examplePath = "open-data-master/data/matches/2/44.json"

# Create json controller
jsonCtrl = jsonController()

# Add example path to json controller
jsonCtrl.addJsonFileToCategory(examplePath, "Matches")

# Get all the values associated with the key/value pair
valuesList = jsonCtrl.getAllValuesFromKeyAtIndex("Matches", "0", "match_id")

print(valuesList)

