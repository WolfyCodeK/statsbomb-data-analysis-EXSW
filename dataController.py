import json

def jsonToString(path):
    with open(path, "r") as read_file:
        strJson = json.load(read_file)
    return strJson