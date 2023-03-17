from jsonController import *

lineupsDir = "open-data-master/data/lineups"

# Create json controller
jsonCtrl = jsonController()

# Add all lineup jsons to the Lineups category
jsonCtrl.addDirectoryToCategory(lineupsDir, "Lineups")

# Get all the values associated with a key, from a chosen category
jsonList = jsonCtrl.getAllValuesInCategoryFromKey("Lineups", "team_name")

# Remove duplicate data
jsonList = list(dict.fromkeys(jsonList))

# Sort in descending order (inefficent sort for large data sets)
jsonList.sort(reverse=False)

# Print out all values
listSize = len(jsonList)

for i in range(listSize):
    print(str(jsonList[i]))
    
print("\nUnique number of teams: " + str(listSize))
