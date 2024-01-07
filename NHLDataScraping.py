from nhlpy import NHLClient

client = NHLClient()

Ari = client.schedule.get_schedule_by_team_by_month('ARI')
##print(str(Ari))

test = client.game_center.score_now()
print(str(test))