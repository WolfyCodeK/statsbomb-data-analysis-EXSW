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
print("Database build time: " + str(round(end - start, 3)) + " seconds")
print("##########################################\n")

start = time.time()

# QUERIES
# Example SQL query
database.printDatabaseQuery("SELECT * FROM TEAM WHERE country_id=68;")

end = time.time()

print("\n#################################################")
print("Database query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")