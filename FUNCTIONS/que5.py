def same(a, b):
    if len(a) == len(b):
        return True
    else:
        return False

a=input("Enter a string: ")
b=input("Enter another string:")
print(same(a,b))