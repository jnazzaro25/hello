 
b = float(input("Enter Coefficient:"))
p = float(input("Enter Probablity of Winning:"))
q = float(input("Enter Probablity of Losing:"))

float(b)
float(p)
float(q)

Result = (((float(b)*float(p))-float(q))/float(b))

Result = Result*100

print("Kelly Criterion suggests:")
print(Result + "Of your current bankroll to be used on this bet.")