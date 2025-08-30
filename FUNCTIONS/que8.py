def minimum(a,b):
    c=a%10
    d=b%10
    if c>d:
        return b
    elif c<d:
        return a
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(minimum(a,b))