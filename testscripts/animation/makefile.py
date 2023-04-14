import time,json

gamefile="largefiles/g2312135_SecondSpectrum_tracking-produced.jsonl"
with open(gamefile, 'r') as json_file:
    json_list = list(json_file)

firsthalflist,secondhalflist=[],[]

for json_str in json_list:
    result = json.loads(json_str)
    tmp_list=[]
    #print(f"result: {result}")
    #print(isinstance(result, dict))
    if result['period'] == 1:
        for element in result['homePlayers']:
            tmp_list.append(element['xyz'])
        for element in result['awayPlayers']:
            tmp_list.append(element['xyz'])
        tmp_list.append(result['ball']['xyz'])
        firsthalflist.append(tmp_list)
    if result['period'] == 2:
        for element in result['homePlayers']:
            tmp_list.append(element['xyz'])
        for element in result['awayPlayers']:
            tmp_list.append(element['xyz'])
        tmp_list.append(result['ball']['xyz'])
        secondhalflist.append(tmp_list)

ffhalfdata=[[] for x in range(23)]
fshalfdata=[[] for x in range(23)]

for element in firsthalflist:
    for i in range(len(element)):
        ffhalfdata[i].append(element[i])

for element in secondhalflist:
    for i in range(len(element)):
        fshalfdata[i].append(element[i])
        

print(len(ffhalfdata),len(fshalfdata))
time.sleep(10)
print(len(ffhalfdata[0]))
print(len(fshalfdata[0]))
'''




'''