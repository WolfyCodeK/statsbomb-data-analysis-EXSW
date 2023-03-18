from enum import Enum

class InsertExpressions(Enum):
    COMPETITIONS_INSERT = 1
    SEVENTS_INSERT = 2
    LINEUPS_INSERT = 3
    MATCHES_INSERT = """ INSERT INTO MATCHES (match_id, match_date, kick_off, home_score,
        away_score, match_status, match_status_360, last_updated, last_updated_360,
        match_week) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    MATCHES_COMPETITION_INSERT = """ INSERT INTO MATCHES_COMPETITION (match_id, competition_id,
        country_name, competition_name) values(?, ?, ?, ?)
    """
    MATCHES_SEASON_INSERT = """ INSERT INTO MATCHES_SEASON (match_id, season_id,
        season_name) values(?, ?, ?)
    """
    MATCHES_HOME_TEAM_INSERT = """ INSERT INTO MATCHES_HOME_TEAM (match_id, home_team_id,
        home_team_name, home_team_gender, home_team_group) values(?, ?, ?, ?, ?)
    """
    MATCHES_HOME_TEAM_COUNTRY_INSERT = """ INSERT INTO MATCHES_HOME_TEAM_COUNTRY (match_id, home_team_id,
        id, name) values(?, ?, ?, ?)
    """
    THREE_SIXTY_INSERT = 5
