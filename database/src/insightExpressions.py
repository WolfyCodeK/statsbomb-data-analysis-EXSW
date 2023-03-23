from enum import Enum

def getQueryNumOfPassesBetweenPlayers(player1, player2):  
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