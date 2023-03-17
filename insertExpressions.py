from enum import Enum

class InsertExpressions(Enum):
    COMPETITIONS_INSERT = 1
    SEVENTS_INSERT = 2
    LINEUPS_INSERT = 3
    MATCHES_INSERT = """ INSERT INTO MATCHES (match_id, match_date, kick_off, home_score,
        away_score, match_status, match_status_360, last_updated, last_updated_360,
        match_week) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    THREE_SIXTY_INSERT = 5
