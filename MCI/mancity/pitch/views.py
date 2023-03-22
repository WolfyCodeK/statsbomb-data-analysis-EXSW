from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    passtest()
    return render(request, 'pitch/pitch.html')


def passtest():
    import json
    print("passtest")

    output = 'pitch/static/pitch/ManCity_Arsenal_events.json'

    # Load the JSON data
    with open(output, 'r') as file:
        data = json.load(file)

    # Specify the player names or IDs
    sender_player_name = "10252"
    receiver_player_name = "10185"

    # figure out how to find different pass types
    for event in data:
        if 'pass' in event:
            print(event)
