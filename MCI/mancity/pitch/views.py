import os
import time
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
    context = {}
    statsbombDB = sl.connect(LOCAL_PATH + "\pitch\database\statsbombDatabase.db")
    dbCursor = statsbombDB.cursor()

    players = get_unique_players()
    pass_count = 0
    sender_id = None
    receiver_id = None
    matchID = 3852832
    teamID = 746

    query = getAllPassesFromMatch(matchID)
    dbCursor.execute(query)
    rows = dbCursor.fetchall()

    if request.method == "POST":
        print("Post req")
        sender_id = request.POST.get("sender")
        receiver_id = request.POST.get("receiver")
        pass_count = passtest(sender_id, receiver_id)
        context={'players': players, 'pass_count': pass_count, 'sender_id': sender_id, 'receiver_id': receiver_id}
        query = getQueryPassesBetweenPlayers(matchID, player1=sender_id, player2=receiver_id)
        dbCursor.execute(query)

        rows = dbCursor.fetchall()
        #len rows is passcount
        if len(rows) != 0:
            pass_count=len(rows)
            times=[]
            for row in rows:
                second = f"{row[3]:02}"
                times.append(f'{row[2]}:{second} - {row[4]}')
            context['times'] = times

        '''
        Xcoord, y coord, min, second
        '''
        context['pass_count']=pass_count
    
    query = getAllTeamPossessions(matchID, teamID)
    dbCursor.execute(query)
    teamPossessions = dbCursor.fetchall()


    # Do something with possession ranking
    possessionRanking = createPossessionRanking(teamPossessions)

    #convert from player ids to string
    print(players)
    for sequence in possessionRanking:
        if sequence[0] > 10:
            temp_list=[]
            #convert player id to string
            for i in range(len(sequence[1])):
                sequence[1][i] = players[str(sequence[1][i])]
    
    actualposessionranking=[]
    #delete if score is less than 10
    for item in possessionRanking:
        if int(item[0]) > 10:
            actualposessionranking.append(item)    
    

    context['players']=players     
    context['possessionRanking'] =actualposessionranking
    return render(request, 'pitch/pitch.html', context)

def createPossessionRanking(teamPossessions):
    # First possession in a match always starts from kick off position
    startxPos = 60
    endxPos = 60
    previousPossession = None
    
    rewardGrowthRate = 1.039
    possessionRanking = []
    passingData = []
    matchTimeSeconds = 0
    
    for passPlay in teamPossessions:
        
        currentPossession = passPlay[0]
        
        # Same possession
        if (currentPossession == previousPossession):
            passingData.append(passPlay[3])
            endxPos = passPlay[2]
            
        # New possession
        if (currentPossession != previousPossession):
            previousPossession = currentPossession
            
            passRecipient = passPlay[4]
            if (passRecipient != None):
                passingData.append(passRecipient)
            
            # Calculate how good the passing possession was
            groundGained = endxPos - startxPos
            pitchPosAdjustmentValue = (pow(rewardGrowthRate, endxPos) / 100)
            possessionValue = groundGained * pitchPosAdjustmentValue    
            
            possessionRanking.append((possessionValue, passingData, matchTimeSeconds))
            passingData = []
            
            # Get value for starting position in new possession
            startxPos = passPlay[1]
            minute = passPlay[5]
            second = passPlay[6]
            matchTimeSeconds = minute * 60 + second
    
    # Sort possession ranking in descending order
    for j in range(len(possessionRanking) - 1):
        for i in range(len(possessionRanking) - 1):
            value = possessionRanking[i][0]
            nextValue = possessionRanking[i+1][0]
            
            if (nextValue > value):
                temp = (value, possessionRanking[i][1], possessionRanking[i][2])
                possessionRanking[i] = (nextValue, possessionRanking[i+1][1], possessionRanking[i+1][2])
                possessionRanking[i+1] = temp  
    
    print(possessionRanking)
    return possessionRanking

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


import os
import zipfile
from django.http import FileResponse

def download_time(request, time):
    # Assume the pre-zipped folder is named "output_files.zip"
    zip_filename = "pitch/output_files.zip"

    import subprocess
    subprocess.call([r'pitch\scriptforobj.bat',time])
    
    # Check if the zip file exists
    if not os.path.exists(zip_filename):
        return HttpResponse("Error: The requested zip file does not exist.", status=404)

    # Serve the pre-zipped folder
    response = FileResponse(open(zip_filename, "rb"), content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={zip_filename}"
    return response

def key_passes(passers,balllocs):

    #turn player passes into list of names
    names = [name[0] for name in passers]
    #turn player passes into tuples (from,to)
    tuples_passes = [(names[i], names[i+1]) for i in range(len(names)-1)]