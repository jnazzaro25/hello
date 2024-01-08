def DisposalsPerGame(Disposals):
    DisposalsPerGame = Disposals/80 ##Team Disposals average per minutes 
    return DisposalsPerGame
def DroppedMarks(): #An uncontested marking opp that is dropped, resulting in a contest at ground level. Does not include Clangers because they are inside the 50. 
    return DroppedMarks
def ScorePerGame(TotalScore):
    ScorePerGame = TotalScore/80  
    return ScorePerGame
def GoalsperGame(Goals):
    GoalsperGame = Goals/80  
    return GoalsperGame
def BehindPerGame(Behinds):
    BehindPerGame = Behinds/80 
    return BehindPerGame
def LeadMarkPerGame(LeadMarks):
    LeadMarkPerGame = LeadMarks/80
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


