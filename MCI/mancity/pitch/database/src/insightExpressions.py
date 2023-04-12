def getQueryPassesBetweenPlayers(matchID, player1, player2):
    query = """
        SELECT location_x, location_y, minute, second, period
        FROM (
            SELECT EVENT.id, event_type_id, match_id, EVENT.player_id, location_x, location_y, minute, second, period
            FROM EVENT
            JOIN PLAYER ON EVENT.player_id = PLAYER.id
        ) AS T1 JOIN PASS ON PASS.event_id = T1.id
        WHERE (event_type_id = 30 AND match_id = """ + str(matchID) + """)
        AND ((T1.player_id = """ + str(player1) + """
        AND recipient_id = """+ str(player2) + """)
        OR (T1.player_id = """ + str(player2) + """
        AND recipient_id = """ + str(player1) + """))
    """

    return query
    
def getMatchID(team1, team2):
    query = """
        SELECT id
        FROM MATCH
        WHERE home_team_id = """ + str(team1) + """
        AND away_team_id = """ + str(team2) + """
    """
    
    return query

def getMatchIDFromTeam(team):
    query = """
        SELECT T1.id, T2.team_name as Home, T3.team_name as Away
        FROM MATCH as T1
        JOIN TEAM as T2 ON T1.home_team_id = T2.id
        JOIN TEAM as T3 ON T1.away_team_id = T3.id
        WHERE T2.id = """ + str(team) + """
        OR T3.id = """ + str(team) + """
    """

def getAllPassesFromMatch(matchID):
    query = """
        SELECT PLAYER.name
        FROM EVENT
        JOIN PLAYER ON EVENT.player_id = PLAYER.id
        WHERE event_type_id = 30 AND match_id = """ + str(matchID) + """
    """
    
    return query

def getAllBallPassLocationsFromMatch(matchID):
    query = """
        SELECT location_x, location_y, end_location_x, end_location_y
        FROM EVENT
        JOIN PASS ON PASS.event_id = EVENT.id
        WHERE event_type_id = 30 AND match_id = """ + str(matchID) + """
    """
    
    return query

def getMaxMatchLength(matchID):
    query = """
        SELECT minute, max(second)
        FROM EVENT JOIN (
            (
                SELECT max(minute) as maxMin
                FROM EVENT
                WHERE match_id = """ + str(matchID) + """
            ) AS T1
        ) ON maxMin = minute
        WHERE match_id = """ + str(matchID) + """
    """
    
    return query

def getAllTeamPossessions(matchID, possessionTeamID):
    query = """
        SELECT possession, location_x, end_location_x, player_id, recipient_id, minute, second
        FROM "EVENT" JOIN PASS ON id = event_id 
        WHERE possession_team_id = """ + str(possessionTeamID) + """ 
        AND event_type_id = 30
        AND match_id = """ + str(matchID) + """;
    """
    
    return query
