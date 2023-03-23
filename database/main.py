from databaseController import *
import time

DATA_PATH = "statsbombdata"

start = time.time()

database = databaseController(DATA_PATH)

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