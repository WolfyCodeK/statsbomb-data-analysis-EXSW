from jsonUtils import *
from formattedDataHandler import *

from enumInsertSQL import *
from enumCategoryNames import *
from enumTablesSQL import *

import os
import sqlite3 as sl

class DatabaseController:
    DATABASE_FILE = "database\statsbombDatabase.db"
    
    def __init__(self, dataPath, build):
        """
        Initialize the database connections.
        
        Args:
            dataPath: File path to the statsbomb open-data-master\data folder
        """
        self.DATA_PATH = dataPath
        self.__openConnections()
        
        if build:
            self.buildDatabase()
        pass
    
    def __deleteDatabase(self):
        """
        Closes connections to database and removes the db file.
        """
        self.__closeConnections()
        os.remove(self.DATABASE_FILE)
        
    def __openConnections(self):
        """
        Opens connections to database and creates a cursor to execute SQL
        expressions through.
        """
        self.statsbombDB = sl.connect(self.DATABASE_FILE)
        
        self.dbCursor = self.statsbombDB.cursor()
        
    def __closeConnections(self):
        """
        Closes the databases connections to free up resources
        """
        # 
        self.dbCursor.close()
        self.statsbombDB.close()
        
    def buildDatabase(self):
        print('> Please wait while database builds...')
        
        if os.path.exists(self.DATABASE_FILE):
            self.__deleteDatabase()
            
        # Create new database
        self.__openConnections()
        
        self.__createTables()
        self.__addAllDirectoriesToDB(self.DATA_PATH) 
        pass
        
    def __addCategoryDirectoryToDB(self, directory, Category: CategoryNames):
        """
        addDirectoryToDB - Adds all json files from a directory into a database.

        Args:
            directory: The relative path to a folder of json files
        """
        if not(os.path.exists(directory)):
            print("FilePathError: the path '" + self.DATA_PATH + "' is not valid a directory")
            os._exit(1)
        
        for filePath in os.listdir(directory):  
            # Get each specific file path in the directory
            file = os.path.join(directory, filePath) 

            if os.path.isfile(file):
                
                # Get the file's extension 
                ext = os.path.splitext(file)[-1].lower()
                
                if ext == ".json":
                    if Category.value in str(file):
                        # Isolate filename from extension
                        deserializedJson = getDeserializedJsonFromFile(file)
                        
                        self.__extractAndStoreData(deserializedJson, str(file))
            else:
                # Recursively call function on folder to traverse through directory
                self.__addCategoryDirectoryToDB(file, Category)  
                
    def __addAllDirectoriesToDB(self, Directory):
        self.__addCategoryDirectoryToDB(Directory, CategoryNames.MATCHES)
        self.__addCategoryDirectoryToDB(Directory, CategoryNames.EVENTS)
                
    def __sqlInsertExpression(self, data, table: InsertSQL):
        self.dbCursor.executemany(table.value, data)
        self.statsbombDB.commit()  

    def getDatabaseQueryResult(self, query):
        self.dbCursor.execute(query)
        rows = self.dbCursor.fetchall()
        
        return rows

    def printDatabaseQuery(self, query):
        result = self.getDatabaseQueryResult(query)
        
        SEPARATOR = "---------------------------------------------------------"

        print(SEPARATOR)
        print(">> QUERY EXPRESSION:")
        print(query)
        print("")
        print(">> QUERY RESULTS:\n")
        
        count = 0
        
        print(SEPARATOR)
        
        for row in result:
            result = str(row)
            result = result.removeprefix("('")
            result = result.removesuffix("',)")
            print("|" + result, end="")
            print("|")
            print(SEPARATOR)
            count += 1
        
        print("\n>> MATCHES FOUND: " + str(count)) 
        print(SEPARATOR)
        
    def __createTables(self):
        """
        Create all the tables required for storing the statsbomb data
        """
        for query in [e.value for e in TableCreationSQL]:
            self.dbCursor.execute(query)
        
    def __extractAndStoreData(self, deserializedJson, fileName):
        # Cast deserializedJson as a list object
        jsonData = list(deserializedJson)
        
        # Check that list is not empty
        if jsonData:
            if CategoryNames.COMPETITIONS.value in fileName:
                pass
            elif CategoryNames.EVENTS.value in fileName:  
                teamIDs = []
    
                # Find the IDs if the teams playing in this event
                for i in range(len(jsonData)):
                    jsonDict = jsonData[i]
                    eventTypeID = jsonDict["type"]["id"]
                    
                    if eventTypeID == 35:
                        teamIDs.append(jsonDict["team"]["id"])     
                
                # Find the matchID of this specific event
                database = DatabaseController(getLocalDataPath(), False)
                result = database.getDatabaseQueryResult(getMatchID(teamIDs[0], teamIDs[1]))
                matchID = str(result[0])
                matchID = matchID.removeprefix("(")
                matchID = matchID.removesuffix(",)")
                
                self.__sqlInsertExpression(getEventData(jsonData, matchID), InsertSQL.EVENT_INSERT)
                self.__sqlInsertExpression(getEventTypeData(jsonData), InsertSQL.EVENT_TYPE_INSERT)
                self.__sqlInsertExpression(getPlayPatternData(jsonData), InsertSQL.PLAY_PATTERN_INSERT)
                self.__sqlInsertExpression(getPlayerData(jsonData), InsertSQL.PLAYER_INSERT)
                self.__sqlInsertExpression(getPassData(jsonData), InsertSQL.PASS_INSERT)
                self.__sqlInsertExpression(getPassTypeData(jsonData), InsertSQL.PASS_TYPE_INSERT)
                self.__sqlInsertExpression(getPassHeightData(jsonData), InsertSQL.PASS_HEIGHT_INSERT)
                        
                pass
            elif CategoryNames.LINEUPS.value in fileName:
                pass
            elif CategoryNames.MATCHES.value in fileName:       
                self.__sqlInsertExpression(getMatchData(jsonData), InsertSQL.MATCH_INSERT)
                self.__sqlInsertExpression(getCompetitionData(jsonData), InsertSQL.COMPETITION_INSERT)
                self.__sqlInsertExpression(getSeasonData(jsonData), InsertSQL.SEASON_INSERT)
                self.__sqlInsertExpression(getHomeTeamData(jsonData), InsertSQL.TEAM_INSERT)
                self.__sqlInsertExpression(getAwayTeamData(jsonData), InsertSQL.TEAM_INSERT)
                self.__sqlInsertExpression(getHomeTeamCountryData(jsonData), InsertSQL.COUNTRY_INSERT)
                self.__sqlInsertExpression(getAwayTeamCountryData(jsonData), InsertSQL.COUNTRY_INSERT)   
                self.__sqlInsertExpression(getHomeTeamManagerData(jsonData), InsertSQL.MANAGER_INSERT)
                self.__sqlInsertExpression(getAwayTeamManagerData(jsonData), InsertSQL.MANAGER_INSERT)
                self.__sqlInsertExpression(getMetadataData(jsonData), InsertSQL.METADATA_INSERT)
                self.__sqlInsertExpression(getCompetitionStageData(jsonData), InsertSQL.COMPETITION_STAGE_INSERT)
                self.__sqlInsertExpression(getStadiumData(jsonData), InsertSQL.STADIUM_INSERT)
                self.__sqlInsertExpression(getRefereeData(jsonData), InsertSQL.REFEREE_INSERT)  
                              
            elif CategoryNames.THREE_SIXTY.value in fileName:
                pass  
            