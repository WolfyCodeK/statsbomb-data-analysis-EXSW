import json
import os
from categories import Categories

class jsonController:
    CATEGORY_ERROR = "ERROR: Invalid category selected"
    ID_ERROR = "ERROR: Invalid id selected"
    NOT_JSON_ERROR = "ERROR: Not a json file"
    NOT_FILE_ERROR = "ERROR: Not a file"
    
    def __init__(self):
        """
        Initialize the json controller's dictionary.
        """
        # Init categorization of json objects as a dictionary of dictionaries
        self.jsonDict = {
            Categories.COMPETITIONS: {},
            Categories.EVENTS: {},
            Categories.LINEUPS: {},
            Categories.MATCHES: {},
            Categories.THREE_SIXTY: {}
        }
        
    @staticmethod
    def __getJsonDeserializedFromFile(path):
        """ 
        __getJsonDeserializedFromFile - Converts a JSON file to a python object.
        
        Args:
            path: Relative path to json file
            return: The python object containing the deserialized json file
        """
        with open(path, "r", encoding="utf8") as read_file:
            jsonDeserialized = json.load(read_file)
            
        return jsonDeserialized
    
    def addJsonFileToCategory(self, path, jsonID, category: Categories=Categories.COMPETITIONS):
        """
        addJsonFileToCategory - Adds a json file to the json controller's dictionary

        Args:
            path: Relative path to json file
            jsonID: The ID of the json being queried (name of the json file)
            category: The category being queried
        """
        # Create json object from file
        jsonDeserialized = self.__getJsonDeserializedFromFile(path)
        
        # Add the json object to the controller's json object dictionary
        if category in self.jsonDict:
            self.jsonDict[category][jsonID] = jsonDeserialized
        else:
            print(self.CATEGORY_ERROR + " -> addJsonFileToCategory()")
    
    def getValueFromKeyAtIndex(self, jsonID, index, key, category: Categories):
        """ 
        getValueFromKey - Gets the value from a key/value pair.
        
        Args:
            jsonID: The ID of the json being queried (name of the json file)
            index: The index position to query in the json file
            key: The value found from a key/value pair
            category: The category being queried 
            
        Returns: 
            value: The value linked to the parsed key, if no value is
                    found then function returns "NULL_VALUE"
        """
        value = "NULL_VALUE"
        
        # Check for valid category
        if category in self.jsonDict:
            # Check for valid jsonID
            if jsonID in self.jsonDict[category].keys():
                # Get value from key/value pair
                value = self.jsonDict[category][jsonID][index][key]
            else:
                print(self.ID_ERROR + " -> getValueFromKeyAtIndex()")
        else:
            print(self.CATEGORY_ERROR + " -> getValueFromKeyAtIndex()")
            
        return value
    
    def getAllValuesInCategoryFromKey(self, key, category: Categories):
        """
        getAllValuesInCategoryFromKey - Gets all the values from all the key/value pair.

        Args:
            key: The value found from a key/value pair
            category: The category being queried 

        Returns:
            valuesList: The list of all the values returned
        """
        values = []
        
        # Loop through all jsons within the category
        for jsonID in self.jsonDict[category].keys():
            # Loop through all the list values within the json
            for i in range(len(self.jsonDict[category][jsonID])):
                values.append(self.getValueFromKeyAtIndex(jsonID, i, key, category))
            
        return values
    
    def addDirectoryToCategory(self, directory, category: Categories):
        """
        addDirectoryToCategory - Adds all json files from a directory into a chosen category.

        Args:
            directory: The relative path to a folder of json files
            category: The category to place the json files into
        """
        for filePath in os.listdir(directory):  
            # Get each specific file path in the directory
            file = os.path.join(directory, filePath)  
                 
            if os.path.isfile(file):
                # Get the file's extension 
                ext = os.path.splitext(file)[-1].lower()
                
                if ext == ".json":
                    # Isolate filename from extension
                    jsonID = str(filePath).removesuffix(".json")
                    self.addJsonFileToCategory(str(directory + "/" +  filePath), jsonID, category)
                else:
                    print(self.NOT_JSON_ERROR + " -> addDirectoryToCategory()")
            else:
                print(self.NOT_FILE_ERROR + " -> addDirectoryToCategory()")
