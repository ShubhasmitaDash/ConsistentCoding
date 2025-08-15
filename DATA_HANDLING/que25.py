import math
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=math.pow(a,3)+math.pow(b,3)+3*math.pow(a,2)*b+3*a*math.pow(b,2)
print("Value of expression is:",c)