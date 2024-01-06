from nhlscrapi.games.game import Game,GameKey,GameType
from nhlscrapi.games.cumstats import Score,ShotCt,Corsi,Fenwick

Season = 2023
game_num = 1 
Game_Type = GameType.Regular
game_key = GameKey(Season,Game_Type,game_num)

cum_stats = {
    'Score': Score(),
    'Shots': ShotCt(),
    Corsi: Corsi(),
    Fenwick: Fenwick()
}
game = Game(game_key,cum_stats = cum_stats)
print(game)

