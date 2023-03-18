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
                
    def __sqlInsertExpression(self, data, table: InsertExpressions):
        self.dbCursor.executemany(table.value, data)
        self.statsbombDB.commit()  
        
    def printDatabaseQuery(self, query):
        self.dbCursor.execute(query)

        rows = self.dbCursor.fetchall()
        separator = "---------------------------------------------------------"

        print(separator)
        print("QUERY EXPRESSION:\n")
        print(query)
        print("\n")
        print(separator)
        print("QUERY RESULTS:\n")
        
        for row in rows:
            print(row)
        
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
                competition_id INTEGER,
                season_id INTEGER,
                home_team_id INTEGER,
                away_team_id INTEGER,
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
                id INTEGER,
                country_name TEXT,
                competition_name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # SEASON
        self.dbCursor.execute(
            """
            CREATE TABLE SEASON (
                id INTEGER,
                season_name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # TEAM
        self.dbCursor.execute(
            """
            CREATE TABLE TEAM (
                id INTEGER,
                team_name TEXT,
                team_gender TEXT,
                team_group TEXT,
                country_id INTEGER,
                manager_id INTEGER,
                PRIMARY KEY (id)
            )
            """
        )
        
        # COUNTRY
        self.dbCursor.execute(
            """
            CREATE TABLE COUNTRY (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
         # MANAGER
        
        # MANAGER
        self.dbCursor.execute(
            """
            CREATE TABLE MANAGER (
                id INTEGER,
                name TEXT,
                nickname TEXT,
                dob TEXT,
                country_id INTEGER,
                PRIMARY KEY (id)
            )
            """
        )
        
        # METADATA
        self.dbCursor.execute(
            """
            CREATE TABLE METADATA (
                match_id INTEGER,
                data_version TEXT,
                shot_fidelity_version TEXT,
                xy_fidelity_version TEXT,
                PRIMARY KEY (match_id)
            )
            """
        )
        
        # COMPETITION_STAGE
        self.dbCursor.execute(
            """
            CREATE TABLE COMPETITION_STAGE (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # STADIUM
        self.dbCursor.execute(
            """
            CREATE TABLE STADIUM (
                id INTEGER,
                name TEXT,
                country_id INTEGER,
                PRIMARY KEY (id)
            )
            """
        )
        
        # REFEREE
        self.dbCursor.execute(
            """
            CREATE TABLE REFEREE (
                id INTEGER,
                name TEXT,
                country_id INTEGER,
                PRIMARY KEY (id)
            )
            """
        )
        
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
                    InsertExpressions.TEAM_INSERT
                )
                
                # AWAY_TEAM
                self.__sqlInsertExpression(
                    getAwayTeamFormattedData(jsonData),
                    InsertExpressions.TEAM_INSERT
                )
                
                # HOME_TEAM_COUNTRY
                self.__sqlInsertExpression(
                    getHomeTeamCountryFormattedData(jsonData),
                    InsertExpressions.COUNTRY_INSERT
                )
                
                # AWAY_TEAM_COUNTRY
                self.__sqlInsertExpression(
                    getAwayTeamCountryFormattedData(jsonData),
                    InsertExpressions.COUNTRY_INSERT
                )
                
                # HOME_TEAM_MANAGER
                self.__sqlInsertExpression(
                    getHomeTeamManagerFormattedData(jsonData),
                    InsertExpressions.MANAGER_INSERT
                )
                    
                # AWAY_TEAM_MANAGER
                self.__sqlInsertExpression(
                    getAwayTeamManagerFormattedData(jsonData),
                    InsertExpressions.MANAGER_INSERT
                )
                    
                # METADATA
                self.__sqlInsertExpression(
                    getMetadataFormattedData(jsonData),
                    InsertExpressions.METADATA_INSERT
                )
               
                # COMPETITION_STAGE
                self.__sqlInsertExpression(
                    getCompetitionStageFormattedData(jsonData),
                    InsertExpressions.COMPETITION_STAGE_INSERT
                )
                
                # STADIUM
                self.__sqlInsertExpression(
                    getStadiumFormattedData(jsonData),
                    InsertExpressions.STADIUM_INSERT
                )
                
                # REFEREE
                self.__sqlInsertExpression(
                    getRefereeFormattedData(jsonData),
                    InsertExpressions.REFEREE_INSERT
                )
                
            elif CategoryNames.THREE_SIXTY.value in fileName:
                pass  
            
              
