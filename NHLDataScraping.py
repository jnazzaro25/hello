import NHLAPIDataConnection as DC 
import json 
import requests
import pandas as pd

URL= 'https://api-web.nhle.com/v1/partner-game/US/now'
team_response = requests.get(URL)
team_response = json.loads(team_response.content)

print(team_response)