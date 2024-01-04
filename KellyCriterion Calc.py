 
b = input("Enter Coefficient:")
p = input("Enter Probablity of Winning:")
q = input("Enter Probablity of Losing:")
odds = input("Enter Current Odds of Bet:")
float(b)
float(p)
float(q)
float(odds)
Result = (((float(b)*float(p))-float(q))/float(b))



if float(odds) > 0:
    Probablity = 100/(odds+100)*100
    
else:
    abs(odds)   
    Probablity = odds/(odds+100)*100

print("This is the Implied Probablity for these Odds" + odds)

print(Result)