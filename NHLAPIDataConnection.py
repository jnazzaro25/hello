## Methods to create the NHL API data connection as well as setup methods to pull data 
import requests
import json
import pandas as pd 

def ConnectionCheck(): ## Check Connection of the NHL API 
    team_Url = 'https://api-web.nhle.com/v1/standings/now'
    team_response =  requests.get(team_Url)
    return team_response


def PullSchedule(date): ## Pulling the schedule based on the date, date must be in YYYY-MM-DD Format 
    team_Url = 'https://api-web.nhle.com/v1/schedule'+ date
    team_response = requests.get(team_Url)
    print(team_Url)
    return team_response


def PullTodaySchedule(): ##Pulling Today's Schedule  
    team_Url = 'https://api-web.nhle.com/v1/schedule/now'
    team_response = requests.get(team_Url)
    return team_response


def FullTeamStats(Team): ##Pulling Full Team Stats by Season need Team Abbreviation 
    team_Url = 'https://api-web.nhle.com/v1/club-stats-season/'+ Team
    team_response = requests.get(team_Url)
    return team_response

def GetOdds(): ##Getting Odds from partner
    URL= 'https://api-web.nhle.com/v1/partner-game/US/now'
    team_response = requests.get(URL)
    team_response = json.loads(team_response.content)
    return team_response