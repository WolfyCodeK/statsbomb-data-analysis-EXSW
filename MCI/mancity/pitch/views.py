import os
from django.shortcuts import render
from django.http import HttpResponse
import json
import sqlite3 as sl
import sys
# Add database path at runtime
LOCAL_PATH = os.getcwd()
sys.path.append(LOCAL_PATH + "\pitch\database\src")
from insightExpressions import *

'''

Select match you want
Select the player you pass from and to
List all the times that event happened



'''

def main(request):
    statsbombDB = sl.connect(LOCAL_PATH + "\pitch\database\statsbombDatabase.db")
    dbCursor = statsbombDB.cursor()

    players = get_unique_players()
    pass_count = 0
    sender_id = None
    receiver_id = None
    matchID = 3852832

    if request.method == "POST":
        sender_id = request.POST.get("sender")
        receiver_id = request.POST.get("receiver")
        pass_count = passtest(sender_id, receiver_id)
        query = getQueryPassesBetweenPlayers(matchID, player1=sender_id, player2=receiver_id)
        dbCursor.execute(query)

        rows = dbCursor.fetchall()
        #len rows is passcount
        if len(rows) != 0:
            pass_count=len(rows)

        '''
        Xcoord, y coord, min, second
        '''

    return render(request, 'pitch/pitch.html', {'players': players, 'pass_count': pass_count, 'sender_id': sender_id, 'receiver_id': receiver_id})

def get_unique_players():

    output = 'pitch/static/pitch/ManCity_Arsenal_events.json'

    # Load the JSON data
    with open(output, 'r', encoding="utf-8") as file:
        data = json.load(file)

    players = {}

    for event in data:
        try:
            if event['type']['name'] == "Pass":
                player_id = str(event['player']['id'])
                player_name = event['player']['name']
                recipient_id = str(event['pass']['recipient']['id'])
                recipient_name = event['pass']['recipient']['name']

                players[player_id] = player_name
                players[recipient_id] = recipient_name
        except:
            pass

    return players

def passtest(sender_id, receiver_id):
    output = 'pitch/static/pitch/ManCity_Arsenal_events.json'

    # Load the JSON data
    with open(output, 'r', encoding="utf-8") as file:
        data = json.load(file)

    pass_count = 0

    for event in data:
        try:
            if event['type']['name'] == "Pass":
                player_id = str(event['player']['id'])
                recipient_id = str(event['pass']['recipient']['id'])

                if player_id == sender_id and recipient_id == receiver_id:
                    pass_count += 1
        except:
            pass

    return pass_count
