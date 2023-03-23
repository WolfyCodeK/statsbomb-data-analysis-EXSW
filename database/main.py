from databaseController import *
import time

DATA_PATH = "statsbombdata"

database = databaseController(DATA_PATH)

buildDB = input("Build database (y/n)?\n> ")

start = time.time()

if buildDB.lower() == 'y':
    database.buildDatabase()

end = time.time()

print("\n##########################################")
print("Database build time: " + str(round(end - start, 3)) + " seconds")
print("##########################################\n")

start = time.time()

# QUERIES
# Example SQL query
database.printDatabaseQuery("SELECT id FROM EVENT WHERE minute=30 AND second=0;")

end = time.time()

print("\n#################################################")
print("Database query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")