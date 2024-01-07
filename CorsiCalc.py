def TeamCorsiFor(ShotsFor,BlocksFor,MissesFor):
    CorsiFor = ShotsFor + BlocksFor + MissesFor
    return CorsiFor
def TeamCorsiAgainst(ShotsAgainst, BlocksAgainst,MissesAgainst):
    CorsiAgainst = ShotsAgainst + BlocksAgainst + MissesAgainst
    return CorsiAgainst
def PercentCorsiFor(CorsiFor,CorsiAgainst):
    PercentCorsi = CorsiFor /(CorsiFor + CorsiAgainst)
    return PercentCorsi
def CorsiAgainstPer60(CorsiAgainst,TOI):
    CorsiAgainstPer60 = CorsiAgainst*60/TOI
    return CorsiAgainstPer60
def CorsiForPer60(CorsiFor,TOI):
    CorsiForPer60 = CorsiFor*60/TOI
    return CorsiForPer60
