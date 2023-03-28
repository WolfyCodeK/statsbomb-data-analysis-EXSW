from databaseController import *
from insightExpressions import *
from jsonUtils import *
import time

dbConfig = getDeserializedJsonFromFile("database\cfg.json")[0]
DATA_PATH = dbConfig["data_src_path"]
SEPARATOR = "##########################################"
QUERY_TIME_DECIMAL_PLACES = 3
TIME_UNITS = " seconds"

start = time.time()

# Init database with path to source data
database = DatabaseController(DATA_PATH)

end = time.time()

print("\n" + SEPARATOR)
print("Database build time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")

start = time.time()

# QUERIES
# Example SQL query
query = getQueryNumOfPassesBetweenPlayers(25632, 25554)
database.printDatabaseQuery(query)

end = time.time()

print("\n" + SEPARATOR)
print("Database query time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")