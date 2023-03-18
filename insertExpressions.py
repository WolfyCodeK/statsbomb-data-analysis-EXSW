from enum import Enum

class InsertExpressions(Enum):
    COMPETITIONS_INSERT = """
    """
    SEVENTS_INSERT = """
    """
    LINEUPS_INSERT = """
    """
    MATCH_INSERT = """ 
        INSERT OR IGNORE INTO MATCH (match_id, match_date, kick_off, home_score,
        away_score, match_status, match_status_360, last_updated, last_updated_360,
        match_week) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    COMPETITION_INSERT = """ 
        INSERT OR IGNORE INTO COMPETITION (competition_id, country_name, competition_name) 
        values(?, ?, ?)
    """
    SEASON_INSERT = """ 
        INSERT OR IGNORE INTO SEASON (season_id, season_name) values(?, ?)
    """
    HOME_TEAM_INSERT = """ 
        INSERT OR IGNORE INTO HOME_TEAM (home_team_id, home_team_name, home_team_gender, 
        home_team_group, country_id, manager_id) values(?, ?, ?, ?, ?, ?)
    """
    COUNTRY_INSERT = """ 
        INSERT OR IGNORE INTO COUNTRY (country_id, name) values(?, ?)
    """
    MANAGER_INSERT = """ 
        INSERT OR IGNORE INTO MANAGER (manager_id, name, nickname, dob, country_id) 
        values(?, ?, ?, ?, ?)
    """
    THREE_SIXTY_INSERT = """
    """
