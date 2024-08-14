## Calculator to take odds and convert it to probablity percentage
a = float(input("What are the odds:"))
odds = 0
if a < 0:
    odds = (-a)/(-a+100)
    print(odds)
else:
    odds = 100/(100+a)
    print(odds)

def Odds(a):
    odds = 0
    if a < 0:
        odds = (-a)/(-a+100)
    else:
        odds = 100/(100+a)
        
