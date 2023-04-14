import time,json

gamefile="largefiles/g2312135_SecondSpectrum_tracking-produced.jsonl"
with open(gamefile, 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    #print(f"result: {result}")
    #print(isinstance(result, dict))
print(result['homePlayers'])
print(result['awayPlayers'])
print(result['ball'])

'''




'''