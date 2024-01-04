from pyAFL.players.models import Player

player = Player("Nick Riewoldt")
player.url
stats = player.get_player_stats()
stats.season_stats_total
