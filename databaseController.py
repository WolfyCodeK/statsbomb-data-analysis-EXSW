from insertExpressions import *
from jsonUtils import *
from categoryNames import *
import os
import sqlite3 as sl

class databaseController:
    SQL_MATHCES_EXPR = "INSERT INTO MATCHES (id, name, age) values(?, ?, ?)"
    DATABASE_FILE = "statsbombDatabase.db"
    
    def __init__(self, dataPath):
        """
        Args:
            dataPath: File path to the statsbomb open-data-master\data folder
        """
        self.DATA_PATH = dataPath
        self.__openConnections()
        pass
    
    def __deleteDatabase(self):
        self.__closeConnections()
        os.remove(self.DATABASE_FILE)
        
    def __openConnections(self):
        self.statsbombDB = sl.connect(self.DATABASE_FILE)
        self.dbCursor = self.statsbombDB.cursor()
        
    def __closeConnections(self):
        # Close database resources
        self.dbCursor.close()
        self.statsbombDB.close()
        
    def __createTables(self):
        # Create matches table
        self.dbCursor.execute(
            """
            CREATE TABLE Matches (
                match_id INTEGER,
                match_date TEXT,
                kick_off TEXT,
                home_score INTEGER,
                away_score INTEGER,
                match_status TEXT,
                match_status_360 TEXT,
                last_updated TEXT,
                last_updated_360 TEXT,
                match_week INTEGER
            )
            """
        )
        
        # Non atomic data within Matches table
        
        # competition
        # season
        # home_team
        # away_team
        # metadata
        # competition_stage
        # stadium
        
    def __sqlInsertExpression(self, data, table: InsertExpressions):
        self.dbCursor.executemany(table.value, data)
        self.statsbombDB.commit()
        
    def __extractAndStoreData(self, deserializedJson, fileName):
        formattedData = []
        
        # Cast deserializedJson as a list object
        jsonData = list(deserializedJson)
        
        # Check that list is not empty
        if jsonData:
            if CategoryNames.COMPETITIONS.value in fileName:
                pass
            elif CategoryNames.EVENTS.value in fileName:
                pass
            elif CategoryNames.LINEUPS.value in fileName:
                pass
            elif CategoryNames.MATCHES.value in fileName:
                for i in range(len(jsonData)):
                    jsonDict = jsonData[i]
                    
                    formattedData.append((
                        jsonDict["match_id"],
                        jsonDict["match_date"],
                        jsonDict["kick_off"],
                        jsonDict["home_score"],
                        jsonDict["away_score"],
                        jsonDict["match_status"],
                        jsonDict["match_status_360"],
                        jsonDict["last_updated"],
                        jsonDict["last_updated_360"],
                        jsonDict["match_week"]
                    ))
                        
                self.__sqlInsertExpression(formattedData, InsertExpressions.MATCHES_INSERT)
            elif CategoryNames.THREE_SIXTY.value in fileName:
                pass   
        
    def buildDatabase(self):
        print('Please wait while database builds...')
        
        if os.path.exists(self.DATABASE_FILE):
            self.__deleteDatabase()
            
        # Create new database
        self.__openConnections()
        
        self.__createTables()
        self.addDirectoryToDB(self.DATA_PATH) 
        pass
        
    def addDirectoryToDB(self, directory):
        """
        addDirectoryToDB - Adds all json files from a directory into a database.

        Args:
            directory: The relative path to a folder of json files
        """
        for filePath in os.listdir(directory):  
            # Get each specific file path in the directory
            file = os.path.join(directory, filePath) 

            if os.path.isfile(file):
                
                # Get the file's extension 
                ext = os.path.splitext(file)[-1].lower()
                
                if ext == ".json":
                    if CategoryNames.MATCHES.value in str(file):
                        # Isolate filename from extension
                        deserializedJson = getDeserializedJsonFromFile(file)
                        
                        self.__extractAndStoreData(deserializedJson, str(file))
            else:
                # Recursively call function on folder to traverse through directory
                self.addDirectoryToDB(file)
        
              
