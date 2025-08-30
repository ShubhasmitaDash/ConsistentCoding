def cube(num=2):
    th=num*num*num
    return th
def equal(a,b):
    if a == b:
        return True
    else:
        return False


n=int(input("Enter a number"))
print(cube())
a=input("Enter one string:")
b=input("Enter another string:")
print(equal(a,b))
