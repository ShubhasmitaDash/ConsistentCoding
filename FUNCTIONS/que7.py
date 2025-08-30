import random as r
def generate(n):
    s="1"
    a="9"
    for i in range(1,n):
        s=s+"0"
        a=a+"9"
    s=int(s)
    a=int(a)
    return r.randint(s,a)

n=int(input("Enter the number of digits:"))
print(generate(n))