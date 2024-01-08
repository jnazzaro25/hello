def DisposalsPerMinute(): ##Team Disposals average per minutes 
    return DisposalsPerMinute
def DroppedMarks(): #An uncontested marking opp that is dropped, resulting in a contest at ground level. Does not include Clangers because they are inside the 50. 
    return DroppedMarks
def ScorePerGame(): 
    return ScorePerGame
def GoalsperGame(): 
    return GoalsperGame
def BehindPerGame(): 
    return BehindPerGame
def LeadMarkPerGame():
    return LeadMarkPerGame
def MissedGoalOppourtunities (ShotsAttempts,Behinds,Goals): #Goal Success Percentage 
    MissedGoalOppourtunities = Goals/(Goals + ShotsAttempts + Behinds)
    return MissedGoalOppourtunities
def ForcedTurnovers(Turnovers, UnforcedTurnovers):
    ForcedTurnovers = Turnovers - UnforcedTurnovers
    return ForcedTurnovers
def ForcedTurnoversPerGame(ForcedTurnovers,TOG):
     ForcedTurnoversPerGame =ForcedTurnovers/TOG
     return ForcedTurnoversPerGame


