from nhlpy import NHLClient
from nhlpy import Teams

client = NHLClient()
golden_knights = Teams.Team(54)
print(golden_knights.stats())

