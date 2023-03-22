from django.shortcuts import render
from django.http import HttpResponse
import json

def main(request):
    passlist = passtest()
    return render(request, 'pitch/pitch.html', {'passlist': passlist})

def passtest():
    print("passtest")

    output = 'pitch/static/pitch/ManCity_Arsenal_events.json'

    # Load the JSON data
    with open(output, 'r', encoding="utf-8") as file:
        data = json.load(file)

    passlist = []

    # Figure out how to find different pass types
    for event in data:
        try:
            if event['type']['name'] == "Pass":
                thedata = str(event['pass']['recipient']['name']) + " recieved the ball from " + str(event['player']['name'])
                passlist.append(thedata)
                print(event['pass']['recipient']['name'] + " recieved the ball from " + event['player']['name'])
        except:
            pass

    return passlist
