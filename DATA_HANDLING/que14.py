import random as rand
while(1):
    a=rand.randrange(100,999)
    if (a%5)==0:
        print(a)
        break
    else:
        continue