from enum import Enum

class TableCreationSQL(Enum):
    MATCHES_TABLE = """
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
    
    COMPETITION_TABLE = """
        CREATE TABLE COMPETITION (
            id INTEGER,
            country_name TEXT,
            competition_name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    SEASON_TABLE = """
        CREATE TABLE SEASON (
            id INTEGER,
            season_name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    TEAM_TABLE = """
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
    
    COUNTRY_TABLE = """
        CREATE TABLE COUNTRY (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    MANAGER_TABLE = """
        CREATE TABLE MANAGER (
            id INTEGER,
            name TEXT,
            nickname TEXT,
            dob TEXT,
            country_id INTEGER,
            PRIMARY KEY (id)
        )
    """
    
    METADATA_TABLE = """
        CREATE TABLE METADATA (
            match_id INTEGER,
            data_version TEXT,
            shot_fidelity_version TEXT,
            xy_fidelity_version TEXT,
            PRIMARY KEY (match_id)
        )
    """
    
    COMPETITION_STAGE_TABLE = """
        CREATE TABLE COMPETITION_STAGE (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    STADIUM_TABLE = """
        CREATE TABLE STADIUM (
            id INTEGER,
            name TEXT,
            country_id INTEGER,
            PRIMARY KEY (id)
        )
    """
    
    REFEREE_TABLE = """
        CREATE TABLE REFEREE (
            id INTEGER,
            name TEXT,
            country_id INTEGER,
            PRIMARY KEY (id)
        )
    """
    
    EVENTS_TABLE = """
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
    
    EVENT_TYPE_TABLE = """
        CREATE TABLE EVENT_TYPE (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    PLAY_PATTERN_TABLE = """
        CREATE TABLE PLAY_PATTERN (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    PLAYER_TABLE = """
        CREATE TABLE PLAYER (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    PASS_TABLE = """
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
    
    PASS_HEIGHT_TABLE = """
        CREATE TABLE PASS_HEIGHT (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """
    
    PASS_TYPE_TABLE = """
        CREATE TABLE PASS_TYPE (
            id INTEGER,
            name TEXT,
            PRIMARY KEY (id)
        )
    """