from databaseController import *
import time

DATA_PATH = "D:\DATA\open-data-master\data"

database = databaseController(DATA_PATH)

buildDB = input("Build database (y/n)?\n> ")

start = time.time()

if buildDB.lower() == 'y':
    database.buildDatabase()

end = time.time()

print("\n##########################################")
print("Total database build time: " + str(round(end - start, 3)) + " seconds")
print("##########################################")

# QUERIES

end = time.time()

print("\n#################################################")
print("Total database build + query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")