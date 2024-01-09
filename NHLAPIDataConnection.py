## Methods to create the NHL API data connection as well as setup methods to pull data 
import requests
import json
import pandas as pd 


team_Url = 'https://api-web.nhle.com/v1/standings/now'
team_response =  requests.get(team_Url)
print(team_response)

