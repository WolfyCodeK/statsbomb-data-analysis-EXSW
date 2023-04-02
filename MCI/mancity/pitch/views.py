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
    context = {}
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
        context={'players': players, 'pass_count': pass_count, 'sender_id': sender_id, 'receiver_id': receiver_id}
        query = getQueryPassesBetweenPlayers(matchID, player1=sender_id, player2=receiver_id)
        dbCursor.execute(query)

        rows = dbCursor.fetchall()
        #len rows is passcount
        if len(rows) != 0:
            pass_count=len(rows)
            times=[]
            for row in rows:
                times.append(f'{row[2]}:{row[3]}')
            print(pass_count)
            print(times)
            context['times'] = times

        '''
        Xcoord, y coord, min, second
        '''
        context['pass_count']=pass_count        
    return render(request, 'pitch/pitch.html', context)

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
    os.system('MCI/mancity/pitch/createmodelmodded.py')

    # Create a ZIP file
    zip_filename = "output_files.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        # Add the output.obj file
        output_obj_file = os.path.join("pitch", "models", "output.obj")
        zipf.write(output_obj_file, "output.obj")

        # Add the output.mtl file
        output_mtl_file = os.path.join("pitch", "models", "theonethatworks.mtl")
        zipf.write(output_mtl_file, "theonethatworks.mtl")

        # Add the textures folder
        textures_folder = os.path.join("pitch", "models", "Textures")
        for folder, subfolders, filenames in os.walk(textures_folder):
            for filename in filenames:
                file_path = os.path.join(folder, filename)
                arcname = os.path.join("Textures", os.path.relpath(file_path, textures_folder))
                zipf.write(file_path, arcname)

    # Serve the ZIP file
    response = FileResponse(open(zip_filename, "rb"), content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={zip_filename}"
    return response
