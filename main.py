from databaseController import *
import time

DATA_PATH = "D:\DATA\open-data-master\data"

# Record start time
start = time.time()

database = databaseController(DATA_PATH)

buildDB = input("Build database (y/n)?\n> ")

if buildDB.lower() == 'y':
    database.buildDatabase()

end = time.time()

print("\n##########################################")
print("Total database build time: " + str(round(end - start, 3)) + " seconds")
print("##########################################")

end = time.time()

# QUERIES

print("\n#################################################")
print("Total database build + query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")