import json

def jsonToString(path):
    """ 
    jsonToString converts a json file to a raw String
    
    Keyword Arguments:
    path: Relative path to json file
    return: Json file in a raw String format   
    """
    with open(path, "r") as read_file:
        strJson = json.load(read_file)
        
    return strJson