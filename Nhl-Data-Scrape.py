##Packages
import pandas as pd 
import datetime as dt 
from random import randint 
from time import sleep 
import os 

## Variables
url = "https://www.hockey-reference.com/leagues/NHL_2022_games.html"
dfs = pd.read_html(url)
df = dfs[0]
dates = pd.to_datetime(df['Date'],format="ISO8601").dt.date
dates = pd.Series(dates).drop_duplicates().tolist()

##Code 
print(dates)
 
