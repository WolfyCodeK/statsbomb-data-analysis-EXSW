import json

def getDeserializedJsonFromFile(path):
    """ 
    Converts a JSON file to a python object.
    
    Args:
        path: Relative path to json file
        return: The python object containing the deserialized json file
    """
    with open(path, "r", encoding="utf8") as read_file:
        deserializedJson = json.load(read_file)
        
    return deserializedJson

def getLocalDataPath():
    dbConfig = getDeserializedJsonFromFile("MCI\mancity\pitch\database\cfg.json")[0]
    DATA_PATH = dbConfig["data_src_path"]
    
    return DATA_PATH

