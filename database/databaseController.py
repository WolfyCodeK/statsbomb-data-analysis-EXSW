from insertExpressions import *
from jsonUtils import *
from categoryNames import *
from formattedDataHandler import *
import os
import sqlite3 as sl

class databaseController:
    SQL_MATHCES_EXPR = "INSERT INTO MATCHES (id, name, age) values(?, ?, ?)"
    DATABASE_FILE = "database\statsbombDatabase.db"
    
    def __init__(self, dataPath):
        """
        Initialize the database connections.
        
        Args:
            dataPath: File path to the statsbomb open-data-master\data folder
        """
        self.DATA_PATH = dataPath
        self.__openConnections()
        
        buildDB = input("> Build database (y/n)?\n> ")
        
        if buildDB.lower() == 'y':
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
        self.addDirectoryToDB(self.DATA_PATH) 
        pass
        
    def addDirectoryToDB(self, directory):
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
                    if CategoryNames.MATCHES.value in str(file):
                        # Isolate filename from extension
                        deserializedJson = getDeserializedJsonFromFile(file)
                        
                        self.__extractAndStoreData(deserializedJson, str(file))
                    if CategoryNames.EVENTS.value in str(file):
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
        print(">> QUERY EXPRESSION:")
        print(query)
        print("\n")
        print(">> QUERY RESULTS:\n")
        
        count = 0
        
        print(separator)
        
        for row in rows:
            result = str(row)
            result = result.removeprefix("('")
            result = result.removesuffix("',)")
            print("|" + result, end="")
            print("|")
            print(separator)
            count += 1
        
        print("\n>> MATCHES FOUND: " + str(count)) 
        print(separator)
    
    def getQueryNumOfPassesBetweenPlayers(self, player1, player2):  
        query = """
            SELECT PassingPlayer.id
            FROM (
                SELECT EVENT.id, PLAYER.name
                FROM EVENT
                JOIN PLAYER ON EVENT.player_id = PLAYER.id
            ) AS PassingPlayer JOIN (
                SELECT PASS.event_id, PLAYER.name
                FROM PASS
                JOIN PLAYER ON PASS.recipient_id = PLAYER.id
            ) AS RecipientOfPass ON id = event_id
            WHERE (PassingPlayer.name = '""" + player1 + """' 
            AND RecipientOfPass.name = '"""+ player2 + """')
            OR (PassingPlayer.name = '""" + player2 + """' 
            AND RecipientOfPass.name = '""" + player1 + """')"""
        
        return query
        
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
        
        # EVENTS
        self.dbCursor.execute(
            """
            CREATE TABLE EVENT (
                id TEXT,
                `index` INTEGER,
                period INTEGER,
                timestamp TEXT,
                minute INTEGER,
                second INTEGER,
                event_type_id INTEGER,
                possession INTEGER,
                possession_team_id INTEGER,
                play_pattern_id INTEGER,
                obv_for_after INTEGER,
                obv_for_before INTEGER,
                obv_for_net INTEGER,
                obv_against_after INTEGER,
                obv_against_before INTEGER,
                obv_against_net INTEGER,
                obv_total_net INTEGER,
                team_id INTEGER,
                player_id INTEGER,
                position_id INTEGER,
                location_x INTEGER,
                location_y INTEGER,
                duration INTEGER,
                formation INTEGER,
                off_camera BOOLEAN,
                out BOOLEAN,
                under_pressure BOOLEAN,
                counterpress BOOLEAN,
                related_events TEXT,
                PRIMARY KEY (id)
            )
            """
            # carry, goalkeeper
        )
        
        # EVENT_TYPE
        self.dbCursor.execute(
            """
            CREATE TABLE EVENT_TYPE (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # PLAY_PATTERN
        self.dbCursor.execute(
            """
            CREATE TABLE PLAY_PATTERN (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # PLAYER
        self.dbCursor.execute(
            """
            CREATE TABLE PLAYER (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # PASS
        self.dbCursor.execute(
            """
            CREATE TABLE PASS (
                event_id TEXT,
                recipient_id INTEGER,
                length INTEGER,
                angle INTEGER,
                height_id INTEGER,
                end_location_x INTEGER,
                end_location_y INTEGER,
                pass_type_id INTEGER,
                body_part_id TEXT,
                PRIMARY KEY (event_id)
            )
            """
        )
        
        # PASS_HEIGHT
        self.dbCursor.execute(
            """
            CREATE TABLE PASS_HEIGHT (
                id INTEGER,
                name TEXT,
                PRIMARY KEY (id)
            )
            """
        )
        
        # PASS_TYPE
        self.dbCursor.execute(
            """
            CREATE TABLE PASS_TYPE (
                id INTEGER,
                name TEXT,
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
                # EVENTS
                self.__sqlInsertExpression(
                    getEventFormattedData(jsonData),
                    InsertExpressions.EVENT_INSERT
                )
                
                # TYPE
                self.__sqlInsertExpression(
                    getEventTypeFormattedData(jsonData),
                    InsertExpressions.EVENT_TYPE_INSERT
                )
                
                # PLAY_PATTERN
                self.__sqlInsertExpression(
                    getPlayPatternFormattedData(jsonData),
                    InsertExpressions.PLAY_PATTERN_INSERT
                )
                
                # PLAYER
                self.__sqlInsertExpression(
                    getPlayerFormattedData(jsonData),
                    InsertExpressions.PLAYER_INSERT
                )
                
                # PASS
                self.__sqlInsertExpression(
                    getPassFormattedData(jsonData),
                    InsertExpressions.PASS_INSERT
                )
                
                # PASS_TYPE
                self.__sqlInsertExpression(
                    getPassTypeFormattedData(jsonData),
                    InsertExpressions.PASS_TYPE_INSERT
                )
                
                # PASS_HEIGHT
                self.__sqlInsertExpression(
                    getPassHeightFormattedData(jsonData),
                    InsertExpressions.PASS_HEIGHT_INSERT
                )
                
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
            
              
