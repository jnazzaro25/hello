def EffFGPercentage(TwoPointersMade,ThreePointersMade,FieldGoalAttempts):
    EffectiveFGPercentage = (TwoPointersMade +(1.5*ThreePointersMade))/FieldGoalAttempts
    return EffectiveFGPercentage
def TrueShootingPercentage(Points,FieldGoalAttempts,FreeThrowAttempts):
    TrueShootingPercentage = Points/(2*(FieldGoalAttempts+(.44*FreeThrowAttempts)))
    return TrueShootingPercentage
