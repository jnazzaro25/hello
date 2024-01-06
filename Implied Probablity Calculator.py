## Calculator to take odds and convert it to probablity percentage
TeamA = float(input("What is the implied odds for the Home Team?:"))
TeamB = float(input("What is the implied odds for the Away Team?:"))

ImpliedTeamA = TeamA/(TeamA + TeamB)
ImpliedTeamB = TeamB/(TeamA + TeamB)
print("The Probablity of the Home Team winning is:" + str(ImpliedTeamA))
print("The Probablity of the Away Team winning is:" + str(ImpliedTeamB))

def ImpliedTeam(TeamA,TeamB):
    TeamA = float(input("What is the implied odds for the Home Team?:"))
    TeamB = float(input("What is the implied odds for the Away Team?:"))

    ImpliedTeamA = TeamA/(TeamA + TeamB)
    ImpliedTeamB = TeamB/(TeamA + TeamB)
