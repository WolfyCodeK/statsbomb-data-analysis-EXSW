import json

class jsonController:
    categoryError = "ERROR: Invalid category selected"
    idError ="ERROR: Invalid id selected"
    
    def __init__(self):
        """
        Initialize the json controller's dictionary.
        """
        # Init categorization of json objects as a dictionary of dictionaries
        self.jsonObjDict = {
            "Competitions": {},
            "Events": {},
            "Lineups": {},
            "Matches": {},
            "Three-sixty": {}
        }
        
    @staticmethod
    def __getJsonObjFromFile(path):
        """ 
        getJsonObjFromFile - Converts a JSON file to a 'json object'.
        
        Args:
            path: Relative path to json file
            return: The json object
        """
        with open(path, "r") as read_file:
            jsonObj = json.load(read_file)
            
        return jsonObj
    
    def addJsonFileToCategory(self, path, catergory):
        """
        addJsonFileToCategory - Adds a json file to the json controller's dictionary

        Args:
            path: Relative path to json file
            catergory: The category being queried
        """
        # Create json object from file
        jsonObj = self.__getJsonObjFromFile(path)
        
        # Add the json object to the controller's json object dictionary
        if catergory in self.jsonObjDict:
            # ["0"] is a place holder until getJsonID() has been implemented
            self.jsonObjDict[catergory]["0"] = jsonObj
        else:
            print(self.categoryError + " -> addJsonFileToCategory()")
    
    def getValueFromKeyAtIndex(self, category, jsonID, index, key):
        """ 
        getValueFromKey - Gets the value from a key/value pair.
        
        Args:
            category: The category being queried 
            jsonID: The ID of the json being queried (name of the json file)
            index: The index position to query in the json file
            key: The value found from a key/value pair
            
        Returns: 
            value: The value linked to the parsed key, if no value is
                    found then function returns "NULL_VALUE"
        """
        value = "NULL_VALUE"
        
        # Check for valid category
        if category in self.jsonObjDict:
            # Check for valid jsonID
            if jsonID in self.jsonObjDict[category]:
                # Get value from key/value pair
                value = self.jsonObjDict[category][jsonID][index][key]
            else:
                print(self.idError)
        else:
            print(self.categoryError + " -> getValueFromKey()")
            
        return value
    
    def getAllValuesFromKeyAtIndex(self, category, jsonID, key):
        valuesList = []
        
        for i in range(len(self.jsonObjDict[category][jsonID])):
            valuesList.append(self.getValueFromKeyAtIndex(category, jsonID, i, key))
            
        return valuesList
    
    def getJsonID():
        pass
        
    
        
        