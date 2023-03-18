def getMatchFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        formattedData.append((
            jsonDict["match_id"],
            jsonDict["match_date"],
            jsonDict["kick_off"],
            jsonDict["competition"]["competition_id"],
            jsonDict["season"]["season_id"],
            jsonDict["home_team"]["home_team_id"],
            jsonDict["away_team"]["away_team_id"],
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

def getHomeTeamCountryFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        homeTeam = jsonDict["home_team"]
        homeTeamCountry = homeTeam["country"]
        
        formattedData.append((
            homeTeamCountry["id"],
            homeTeamCountry["name"]
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getHomeTeamManagerFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        homeTeam = jsonDict["home_team"]
        homeTeamCountry = homeTeam["country"]
        
        if "managers" in homeTeam:
            homeTeamManagers = homeTeam["managers"]
            # TEMP SOLUTION FOR MULTIPLE MANAGERS
            manager = homeTeamManagers[0]
            
            formattedData.append((
                manager["id"],
                manager["name"],
                manager["nickname"],
                manager["dob"],
                homeTeamCountry["id"]
            ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getAwayTeamFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        awayTeam = jsonDict["away_team"]
        awayTeamCountry = awayTeam["country"]
        
        managerID = None
        
        if "managers" in awayTeam:
            awayTeamManagers = awayTeam["managers"]
            # TEMP SOLUTION FOR MULTIPLE MANAGERS
            managerID = awayTeamManagers[0]["id"]
            
        formattedData.append((
            awayTeam["away_team_id"],
            awayTeam["away_team_name"],
            awayTeam["away_team_gender"],
            awayTeam["away_team_group"],
            awayTeamCountry["id"],
            managerID
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getAwayTeamCountryFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        awayTeam = jsonDict["home_team"]
        awayTeamCountry = awayTeam["country"]
        
        formattedData.append((
            awayTeamCountry["id"],
            awayTeamCountry["name"]
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getAwayTeamManagerFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        awayTeam = jsonDict["home_team"]
        awayTeamCountry = awayTeam["country"]
        
        if "managers" in awayTeam:
            awayTeamManagers = awayTeam["managers"]
            # TEMP SOLUTION FOR MULTIPLE MANAGERS
            manager = awayTeamManagers[0]
            
            formattedData.append((
                manager["id"],
                manager["name"],
                manager["nickname"],
                manager["dob"],
                awayTeamCountry["id"]
            ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getMetadataFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        metadata = jsonDict["metadata"]
        
        shotFidelityVersion = None
        xyFidelityVersion = None
            
        if "shot_fidelity_version" in metadata:
            shotFidelityVersion = metadata["shot_fidelity_version"]
            
        if "xy_fidelity_version" in metadata:
            xyFidelityVersion = metadata["xy_fidelity_version"]
        
        formattedData.append((
            jsonDict["match_id"],
            metadata["data_version"],
            shotFidelityVersion,
            xyFidelityVersion
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getCompetitionStageFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        competitionStage = jsonDict["competition_stage"]
        
        formattedData.append((
            competitionStage["id"],
            competitionStage["name"]
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getStadiumFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "stadium" in jsonDict:
            stadium = jsonDict["stadium"]
                
            formattedData.append((
            stadium["id"],
            stadium["name"],
            stadium["country"]["id"]
        ))
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getRefereeFormattedData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "referee" in jsonDict:
            referee = jsonDict["referee"]
                
            formattedData.append((
            referee["id"],
            referee["name"],
            referee["country"]["id"]
        ))
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

