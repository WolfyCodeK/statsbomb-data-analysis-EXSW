def getQueryNumOfPassesBetweenPlayers(player1, player2):
    query = """
        SELECT location_x, location_y, minute, second
        FROM (
            SELECT EVENT.id, EVENT.player_id, location_x, location_y, minute, second
            FROM EVENT
            JOIN PLAYER ON EVENT.player_id = PLAYER.id
        ) AS T1 JOIN PASS ON PASS.event_id = T1.id
        WHERE (T1.player_id = """ + str(player1) + """
        AND recipient_id = """+ str(player2) + """)
        OR (T1.player_id = """ + str(player2) + """
        AND recipient_id = """ + str(player1) + """)
        """

    return query

