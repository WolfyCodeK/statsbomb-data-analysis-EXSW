from insertExpressions import *
from jsonUtils import *
from categoryNames import *
from formattedDataHandler import *
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
        # Create Matches table
        self.dbCursor.execute(
            """
            CREATE TABLE MATCHES (
                match_id INTEGER,
                match_date TEXT,
                kick_off TEXT,
                home_score INTEGER,
                away_score INTEGER,
                match_status TEXT,
                match_status_360 TEXT,
                last_updated TEXT,
                last_updated_360 TEXT,
                match_week INTEGER,
                PRIMARY KEY (match_id)
            )
            """
        )
        
        # Non atomic data within Matches table
        self.dbCursor.execute(
            """
            CREATE TABLE MATCHES_COMPETITION (
                match_id INTEGER,
                competition_id INTEGER,
                country_name TEXT,
                competition_name TEXT,
                PRIMARY KEY (match_id)
            )
            """
        )
        
        self.dbCursor.execute(
            """
            CREATE TABLE MATCHES_SEASON (
                match_id INTEGER,
                season_id INTEGER,
                season_name TEXT,
                PRIMARY KEY (match_id)
            )
            """
        )
        
        self.dbCursor.execute(
            """
            CREATE TABLE MATCHES_HOME_TEAM (
                match_id INTEGER,
                home_team_id INTEGER,
                home_team_name TEXT,
                home_team_gender TEXT,
                home_team_group TEXT,
                PRIMARY KEY (match_id)
            )
            """
        )
        
        self.dbCursor.execute(
            """
            CREATE TABLE MATCHES_HOME_TEAM_COUNTRY (
                match_id INTEGER,
                home_team_id INTEGER,
                id INTEGER,
                name TEXT,
                PRIMARY KEY (match_id, home_team_id)
            )
            """
        )
        # away_team
        # metadata
        # competition_stage
        # stadium
        
    def __sqlInsertExpression(self, data, table: InsertExpressions):
        self.dbCursor.executemany(table.value, data)
        self.statsbombDB.commit()
        
    def __extractAndStoreData(self, deserializedJson, fileName):
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
                self.__sqlInsertExpression(
                    getMatchesFormattedData(jsonData),
                    InsertExpressions.MATCHES_INSERT
                )

                self.__sqlInsertExpression(
                    getMatchesCompetitionsFormattedData(jsonData),
                    InsertExpressions.MATCHES_COMPETITION_INSERT
                )
                
                self.__sqlInsertExpression(
                    getMatchesSeasonFormattedData(jsonData),
                    InsertExpressions.MATCHES_SEASON_INSERT
                )
                
                self.__sqlInsertExpression(
                    getMatchesHomeTeamFormattedData(jsonData),
                    InsertExpressions.MATCHES_HOME_TEAM_INSERT
                )
                
                self.__sqlInsertExpression(
                    getMatchesHomeTeamCountryFormattedData(jsonData),
                    InsertExpressions.MATCHES_HOME_TEAM_COUNTRY_INSERT
                )
                
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
            
              
