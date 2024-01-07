def ShotsForPer60(ShotsFor,TOI):
    ShotsForPer60 = ShotsFor*60/TOI
    return ShotsForPer60
def ShotsAgainstPer60(ShotsAgainst,TOI):
    ShotsAgainstPer60 = ShotsAgainst*60/TOI
    return ShotsAgainstPer60
def FenwickFor(SOGFor,MissedShotsFor):
    FenwickFor = SOGFor + MissedShotsFor
    return FenwickFor
def FenwickAgainst(SOGAgainst,MissedShotsAgainst):
    FenwickAgainst = SOGAgainst + MissedShotsAgainst
    return FenwickAgainst
def Fenwick(FenwickFor,FenwickAgainst):
    Fenwick = FenwickFor - FenwickAgainst
    return
def PercentFenwick(FenwickFor,FenwickAgainst):
    PercentFenwick = (FenwickFor/(FenwickFor +FenwickAgainst))*100
    return PercentFenwick
def GoalsForPer60(Goals,TOI):
    GoalsForPer60 = Goals*60/TOI
    return GoalsForPer60
def GoalsAgainstPer60(GoalsAgainst,TOI):
    GoalsAgainstPer60 = GoalsAgainst*60/TOI
    return GoalsAgainstPer60
def ShootingSuccess(GoalsFor,ShotsOnGoal):
    ShootingSuccess = (GoalsFor/ShotsOnGoal)*100
    return ShootingSuccess
def SavePercentage(GoalsAgainst,ShotsAgainst):
    SavePercentage = (GoalsAgainst/ShotsAgainst)*100
    return SavePercentage
def PDO(ShootingSuccess,SavePercentage):
    PDO = ShootingSuccess + SavePercentage
    return PDO

