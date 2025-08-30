import random as r
def your_range(num1, num2):
    a=r.randint(num1,num2)
    return a

for i in range(0, 3):
    print(your_range(1,10))