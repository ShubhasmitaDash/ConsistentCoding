a=int(input("Enter a 3 digit number:"))
unit=a%10
unit=str(unit)
a=a//10
tens=a%10
tens=str(tens)
a=a//10
hundreds=a
hundreds=str(hundreds)
print(unit+tens+hundreds)