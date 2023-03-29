from databaseController import *
from insightExpressions import *
from jsonUtils import *
import time

SEPARATOR = "##########################################"
QUERY_TIME_DECIMAL_PLACES = 3
TIME_UNITS = " seconds"

start = time.time()

# Init database with path to source data
database = DatabaseController(getLocalDataPath(), True)

end = time.time()

print("\n" + SEPARATOR)
print("Database build time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")

start = time.time()

# QUERIES
# Example SQL query
query = getQueryPassesBetweenPlayers(3855961, 25632, 25554)
database.printDatabaseQuery(query)

end = time.time()

print("\n" + SEPARATOR)
print("Database query time: " + str(round(end - start, QUERY_TIME_DECIMAL_PLACES)) + TIME_UNITS)
print(SEPARATOR + "\n")