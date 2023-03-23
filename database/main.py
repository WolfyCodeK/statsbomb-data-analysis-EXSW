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
query = database.getQueryNumOfPassesBetweenPlayers("Yui Hasegawa", "Khadija Monifa Shaw")
database.printDatabaseQuery(query)

end = time.time()

print("\n#################################################")
print("Database query time: " + str(round(end - start, 3)) + " seconds")
print("#################################################\n")