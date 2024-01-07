def EffFGPercentage(TwoPointersMade,ThreePointersMade,FieldGoalAttempts):
    EffectiveFGPercentage = (TwoPointersMade +(1.5*ThreePointersMade))/FieldGoalAttempts
    return EffectiveFGPercentage
def TrueShootingPercentage(Points,FieldGoalAttempts,FreeThrowAttempts):
    TrueShootingPercentage = Points/(2*(FieldGoalAttempts+(.44*FreeThrowAttempts)))
    return TrueShootingPercentage
def NumOfPosessions(FieldGoalAttempts,FreeThrowAttempts,OffensiveRebounds,Turnovers):
    NumOfPosessions = FieldGoalAttempts - OffensiveRebounds + Turnovers + (0.4*FreeThrowAttempts)
    return NumOfPosessions
def OffensiveEffiency(TotalPoints, NumOfPosessions):
    OffensiveEffiency = TotalPoints/NumOfPosessions
    return OffensiveEffiency
def DefensiveEffiency(PointsAgainst,NumOfPosessions):
    DefensiveEffiency = PointsAgainst/NumOfPosessions
    return DefensiveEffiency
def EffiencyMargin(OffensiveEffiency,DefensiveEffiency):
    EffiencyMargin = OffensiveEffiency - DefensiveEffiency
    return EffiencyMargin
