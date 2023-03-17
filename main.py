from jsonController import *
import time

# Record start time
start = time.time()

competitionsPath = "open-data-master\data\competitions.json"
eventsDir = "open-data-master/data/events"
lineupsDir = "open-data-master/data/lineups"
matchesDir = "open-data-master/data/matches"
threeSixtyDir = "open-data-master/data/three-sixty"

# Create json controller
jsonCtrl = jsonController()

# Add all jsons to their appropriate category 
jsonCtrl.addJsonFileToCategory(competitionsPath, "competitions", category=Categories.COMPETITIONS)
jsonCtrl.addDirectoryToCategory(eventsDir, category=Categories.EVENTS)
jsonCtrl.addDirectoryToCategory(lineupsDir, category=Categories.LINEUPS)
# jsonCtrl.addDirectoryToCategory(matchesDir, category=Categories.MATCHES)
jsonCtrl.addDirectoryToCategory(threeSixtyDir, category=Categories.THREE_SIXTY)

# Record end time
end = time.time()

print("\n##########################################")
print("Total database build time: " + str(round(end - start, 3)) + " seconds")
print("##########################################")

# Get all the values associated with a key, from a chosen category
jsonList = jsonCtrl.getAllValuesInCategoryFromKey("team_name", category=Categories.LINEUPS)

# Remove duplicate data
jsonList = list(dict.fromkeys(jsonList))

# Sort in descending order (inefficent sort for large data sets)
jsonList.sort()

# Print out all values
listSize = len(jsonList)

for i in range(listSize):
    print(str(jsonList[i]))
    
print("\nUnique number of teams: " + str(listSize))

end = time.time()

print("\n#################################################")
print("Total database build + query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")