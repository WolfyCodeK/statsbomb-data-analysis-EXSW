from databaseController import *
from jsonUtils import getDeserializedJsonFromFile
import time

dbConfig = getDeserializedJsonFromFile("database\cfg.json")[0]
DATA_PATH = dbConfig["data_src_path"]
SEPARATOR = "##########################################"
QUERY_TIME_DECIMAL_PLACES = 3
TIME_UNITS = " seconds"

start = time.time()

# Init database with path to source data
database = databaseController(DATA_PATH)

end = time.time()

print("\n" + SEPARATOR)
print("Database build time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")

start = time.time()

# QUERIES
# Example SQL query
query = database.getQueryNumOfPassesBetweenPlayers("Yui Hasegawa", "Khadija Monifa Shaw")
database.printDatabaseQuery(query)

end = time.time()

print("\n" + SEPARATOR)
print("Database query time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")