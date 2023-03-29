def getQueryPassesBetweenPlayers(matchID, player1, player2):
    query = """
        SELECT location_x, location_y, minute, second
        FROM (
            SELECT EVENT.id, match_id, EVENT.player_id, location_x, location_y, minute, second
            FROM EVENT
            JOIN PLAYER ON EVENT.player_id = PLAYER.id
        ) AS T1 JOIN PASS ON PASS.event_id = T1.id
        WHERE (match_id = """ + str(matchID) + """)
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

