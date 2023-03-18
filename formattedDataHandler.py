def getMatchesFormattedData(jsonData) -> list:
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
        
    return formattedData
    
def getMatchesCompetitionsFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictCompetition = jsonDict["competition"]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDictCompetition["competition_id"],
            jsonDictCompetition["country_name"],
            jsonDictCompetition["competition_name"]
        ))
        
    return formattedData

def getMatchesSeasonFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictSeason = jsonDict["season"]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDictSeason["season_id"],
            jsonDictSeason["season_name"]
        ))
        
    return formattedData
    
def getMatchesHomeTeamFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictHomeTeam = jsonDict["home_team"]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDictHomeTeam["home_team_id"],
            jsonDictHomeTeam["home_team_name"],
            jsonDictHomeTeam["home_team_gender"],
            jsonDictHomeTeam["home_team_group"]
        ))
        
    return formattedData

def getMatchesHomeTeamCountryFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        jsonDictHomeTeam = jsonDict["home_team"]
        jsonDictHomeTeamCountry = jsonDictHomeTeam["country"]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDictHomeTeam["home_team_id"],
            jsonDictHomeTeamCountry["id"],
            jsonDictHomeTeamCountry["name"]
        ))
        
    return formattedData