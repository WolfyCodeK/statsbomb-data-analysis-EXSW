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
        Initialize the database connections.
        
        Args:
            dataPath: File path to the statsbomb open-data-master\data folder
        """
        self.DATA_PATH = dataPath
        self.__openConnections()
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
        
    def __createTables(self):
        """
        Create all the tables required for storing the statsbomb data
        """
        # MATCHES
        self.dbCursor.execute(
            """
            CREATE TABLE MATCH (
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
        
        # COMPETITION
        self.dbCursor.execute(
            """
            CREATE TABLE COMPETITION (
                competition_id INTEGER,
                country_name TEXT,
                competition_name TEXT,
                PRIMARY KEY (competition_id)
            )
            """
        )
        
        # SEASON
        self.dbCursor.execute(
            """
            CREATE TABLE SEASON (
                season_id INTEGER,
                season_name TEXT,
                PRIMARY KEY (season_id)
            )
            """
        )
        
        # HOME_TEAM
        self.dbCursor.execute(
            """
            CREATE TABLE HOME_TEAM (
                home_team_id INTEGER,
                home_team_name TEXT,
                home_team_gender TEXT,
                home_team_group TEXT,
                country_id INTEGER,
                manager_id INTEGER,
                PRIMARY KEY (home_team_id)
            )
            """
        )
        
        # COUNTRY
        self.dbCursor.execute(
            """
            CREATE TABLE COUNTRY (
                country_id INTEGER,
                name TEXT,
                PRIMARY KEY (country_id)
            )
            """
        )
        
         # MANAGER
        
        # MANAGER
        self.dbCursor.execute(
            """
            CREATE TABLE MANAGER (
                manager_id INTEGER,
                name TEXT,
                nickname TEXT,
                dob TEXT,
                country_id INTEGER,
                PRIMARY KEY (manager_id)
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
                # MATCH
                self.__sqlInsertExpression(
                    getMatchFormattedData(jsonData),
                    InsertExpressions.MATCH_INSERT
                )

                # COMPETITION
                self.__sqlInsertExpression(
                    getCompetitionFormattedData(jsonData),
                    InsertExpressions.COMPETITION_INSERT
                )
                
                # SEASON
                self.__sqlInsertExpression(
                    getSeasonFormattedData(jsonData),
                    InsertExpressions.SEASON_INSERT
                )
                
                # HOME_TEAM
                self.__sqlInsertExpression(
                    getHomeTeamFormattedData(jsonData),
                    InsertExpressions.HOME_TEAM_INSERT
                )
                
                # COUNTRY
                self.__sqlInsertExpression(
                    getCountryFormattedData(jsonData),
                    InsertExpressions.COUNTRY_INSERT
                )
                
                # MANAGER
                formattedData = getManagerFormattedData(jsonData)
                # Check the senario where there are no managers
                if formattedData:
                    self.__sqlInsertExpression(
                        formattedData,
                        InsertExpressions.MANAGER_INSERT
                    )
                    
                """
                self.__sqlInsertExpression(
                        formattedData,
                        InsertExpressions.MANAGER_INSERT
                    )
                """
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
            
              
