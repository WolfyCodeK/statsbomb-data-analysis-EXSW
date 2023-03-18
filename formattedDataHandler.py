def getMatchFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDict["match_date"],
            jsonDict["kick_off"],
            jsonDict["home_score"],
            jsonDict["away_score"],
            jsonDict["match_status"],
            jsonDict["match_status_360"],
            jsonDict["last_updated"],
            jsonDict["last_updated_360"],
            jsonDict["match_week"]
        ))
        
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData
    
def getCompetitionFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictCompetition = jsonDict["competition"]
        
        formattedData.append((
            jsonDictCompetition["competition_id"],
            jsonDictCompetition["country_name"],
            jsonDictCompetition["competition_name"]
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
    
    return formattedData

def getSeasonFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictSeason = jsonDict["season"]
        
        formattedData.append((
            jsonDictSeason["season_id"],
            jsonDictSeason["season_name"]
        ))
        
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))    
        
    return formattedData
    
def getHomeTeamFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictHomeTeam = jsonDict["home_team"]
        jsonDictHomeTeamCountry = jsonDictHomeTeam["country"]
        
        managerID = None
        
        if "managers" in jsonDictHomeTeam:
            jsonDictHomeTeamManagers = jsonDictHomeTeam["managers"]
            # TEMP SOLUTION FOR MULTIPLE MANAGERS
            managerID = jsonDictHomeTeamManagers[0]["id"]
            
        formattedData.append((
            jsonDictHomeTeam["home_team_id"],
            jsonDictHomeTeam["home_team_name"],
            jsonDictHomeTeam["home_team_gender"],
            jsonDictHomeTeam["home_team_group"],
            jsonDictHomeTeamCountry["id"],
            managerID
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getCountryFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictHomeTeam = jsonDict["home_team"]
        jsonDictHomeTeamCountry = jsonDictHomeTeam["country"]
        
        formattedData.append((
            jsonDictHomeTeamCountry["id"],
            jsonDictHomeTeamCountry["name"]
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getManagerFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictHomeTeam = jsonDict["home_team"]
        jsonDictHomeTeamCountry = jsonDictHomeTeam["country"]
        
        if "managers" in jsonDictHomeTeam:
            jsonDictHomeTeamManagers = jsonDictHomeTeam["managers"]
            # TEMP SOLUTION FOR MULTIPLE MANAGERS
            manager = jsonDictHomeTeamManagers[0]
            
            formattedData.append((
                manager["id"],
                manager["name"],
                manager["nickname"],
                manager["dob"],
                jsonDictHomeTeamCountry["id"]
            ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

