from insightExpressions import *

def getMatchData(jsonData) -> list:
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
    
def getCompetitionData(jsonData) -> list:
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

def getSeasonData(jsonData) -> list:
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
    
def getHomeTeamData(jsonData) -> list:
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

def getHomeTeamCountryData(jsonData) -> list:
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

def getHomeTeamManagerData(jsonData) -> list:
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

def getAwayTeamData(jsonData) -> list:
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

def getAwayTeamCountryData(jsonData) -> list:
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

def getAwayTeamManagerData(jsonData) -> list:
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

def getMetadataData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        metadata = jsonDict["metadata"]
        
        shotFidelityVersion = None
        xyFidelityVersion = None
            
        if "data_version" in metadata:
            dataVersion = metadata["data_version"]    
            
        if "shot_fidelity_version" in metadata:
            shotFidelityVersion = metadata["shot_fidelity_version"]
            
        if "xy_fidelity_version" in metadata:
            xyFidelityVersion = metadata["xy_fidelity_version"]
            
        formattedData.append((
            jsonDict["match_id"],
            dataVersion,
            shotFidelityVersion,
            xyFidelityVersion
        ))
    
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getCompetitionStageData(jsonData) -> list:
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

def getStadiumData(jsonData) -> list:
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

def getRefereeData(jsonData) -> list:
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

def getEventData(jsonData, matchID) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        obvForList = [None, None, None]
        obvAgainstList = [None, None, None]
        obvTotal = None
        playerID = None
        positionID = None
        duration = None
        formation = None
        offCamera = False
        out = False
        underPressure = False
        counterPress = False
        locationX = None
        locationY = None
        strRelatedEvents = None
        
        if "obv_for_after" in jsonDict:
            obvForList.insert(0, jsonDict["obv_for_after"])
            obvForList.insert(1, jsonDict["obv_for_before"])
            obvForList.insert(2, jsonDict["obv_for_net"])
            obvTotal = jsonDict["obv_total_net"]
            
        if "obv_against_after" in jsonDict:
            obvAgainstList.insert(0, jsonDict["obv_against_after"])
            obvAgainstList.insert(1, jsonDict["obv_against_before"])
            obvAgainstList.insert(2, jsonDict["obv_against_net"])
            obvTotal = jsonDict["obv_total_net"]
            
        if "player" in jsonDict:
            playerID = jsonDict["player"]["id"]
        
        if "position" in jsonDict:
            positionID = jsonDict["position"]["id"]
                
        if "location" in jsonDict:
            locationX = jsonDict["location"][0]
            locationY = jsonDict["location"][1]
            
        if "duration" in jsonDict:
            duration = jsonDict["duration"]
            
        if "tactics" in jsonDict:
            formation = jsonDict["tactics"]["formation"]
            
        if "off_camera" in jsonDict:
            offCamera = jsonDict["off_camera"]   
            
        if "out" in jsonDict:
            out = jsonDict["out"]   
            
        if "counter_press" in jsonDict:
            counterPress = jsonDict["counter_press"]
            
        if "under_pressure" in jsonDict:
            underPressure = jsonDict["under_pressure"]
            
        if "related_events" in jsonDict:
            relatedEvents = jsonDict["related_events"]
            strRelatedEvents = ''.join(relatedEvents)
            
        
        formattedData.append((
            jsonDict["id"],
            matchID,
            jsonDict["index"],
            jsonDict["period"],
            jsonDict["timestamp"],
            jsonDict["minute"],
            jsonDict["second"],
            jsonDict["type"]["id"],
            jsonDict["possession"],
            jsonDict["possession_team"]["id"],
            jsonDict["play_pattern"]["id"],
            obvForList[0],
            obvForList[1],
            obvForList[2],
            obvAgainstList[0],
            obvAgainstList[1],
            obvAgainstList[2],
            obvTotal,
            jsonDict["team"]["id"],
            playerID,
            positionID,
            locationX,
            locationY,
            duration,
            formation,
            offCamera,
            out,
            underPressure,
            counterPress,
            strRelatedEvents
        ))
        
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getEventTypeData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        typeData = jsonDict["type"]
                        
        formattedData.append((
            typeData["id"],
            typeData["name"],
        ))
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getPlayPatternData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        playPatternData = jsonDict["play_pattern"]
                        
        formattedData.append((
            playPatternData["id"],
            playPatternData["name"],
        ))
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getPlayerData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "player" in jsonDict:
            player = jsonDict["player"]
             
            formattedData.append((
                player["id"],
                player["name"],
            ))          
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getPassData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "pass" in jsonDict:
            passData = jsonDict["pass"]
            
            recipientID = None
            passTypeID = None
            bodyPartID = None
            
            if "recipient" in passData:
                recipientID = passData["recipient"]["id"]
            
            if "type" in passData:
                passTypeID = passData["type"]["id"]
                
            if "body_part" in passData:
                bodyPartID = passData["body_part"]["id"]
             
            formattedData.append((
                jsonDict["id"],
                recipientID,
                passData["length"],
                passData["angle"],
                passData["height"]["id"],
                passData["end_location"][0],
                passData["end_location"][1],
                passTypeID,
                bodyPartID
            ))          
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getPassHeightData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "pass" in jsonDict:
            passHeight = jsonDict["pass"]["height"]
             
            formattedData.append((
                passHeight["id"],
                passHeight["name"],
            ))          
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

def getPassTypeData(jsonData) -> list:
    formattedData = []
    
    for i in range(len(jsonData)):
        jsonDict = jsonData[i]
        
        if "pass" in jsonDict:
            passData = jsonDict["pass"]
            
            if "type" in passData:
                passType = jsonDict["pass"]["type"]
             
            formattedData.append((
                passType["id"],
                passType["name"],
            ))          
                
    # Remove duplicate tuples
    formattedData = list(dict.fromkeys(formattedData))
        
    return formattedData

