from enum import Enum

class InsertExpressions(Enum):
    COMPETITIONS_INSERT = """
    """
    SEVENTS_INSERT = """
    """
    LINEUPS_INSERT = """
    """
    # MATCH RELATED INSERTS EXPRESSIONS
    MATCH_INSERT = """ 
        INSERT OR IGNORE INTO MATCH (match_id, match_date, kick_off, competition_id,
        season_id, home_team_id, away_team_id, home_score, away_score, match_status, 
        match_status_360, last_updated, last_updated_360, match_week) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    COMPETITION_INSERT = """ 
        INSERT OR IGNORE INTO COMPETITION (id, country_name, competition_name) 
        values(?, ?, ?)
    """
    SEASON_INSERT = """ 
        INSERT OR IGNORE INTO SEASON (id, season_name) values(?, ?)
    """
    TEAM_INSERT = """ 
        INSERT OR IGNORE INTO TEAM (id, team_name, team_gender, 
        team_group, country_id, manager_id) values(?, ?, ?, ?, ?, ?)
    """
    COUNTRY_INSERT = """ 
        INSERT OR IGNORE INTO COUNTRY (id, name) values(?, ?)
    """
    MANAGER_INSERT = """ 
        INSERT OR IGNORE INTO MANAGER (id, name, nickname, dob, country_id) 
        values(?, ?, ?, ?, ?)
    """
    METADATA_INSERT = """ 
        INSERT OR IGNORE INTO METADATA (match_id, data_version, shot_fidelity_version, 
        xy_fidelity_version) values(?, ?, ?, ?)
    """
    COMPETITION_STAGE_INSERT = """ 
        INSERT OR IGNORE INTO COMPETITION_STAGE (id, name) values(?, ?)
    """
    STADIUM_INSERT = """
        INSERT OR IGNORE INTO STADIUM (id, name, country_id) values(?, ?, ?)
    """
    REFEREE_INSERT = """
        INSERT OR IGNORE INTO REFEREE (id, name, country_id) values(?, ?, ?)
    """
    EVENT_INSERT = """
        INSERT OR IGNORE INTO EVENT (id, `index`, period, timestamp,
        minute, second, type_id, possession, possession_team_id, play_pattern_id, 
        obv_for_after, obv_for_before, obv_for_net, obv_against_after, obv_against_before,
        obv_against_net, obv_total_net, team_id, player_id, position_id, location_x, location_y,
        duration, under_pressure, counterpress, related_events) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    # THREE-SIXTY RELATED INSERT EXPRESSIONS
    THREE_SIXTY_INSERT = """
    """
