def volume(length, breadth, height):
    return length * breadth * height

l=int(input("Enter the length of the box: "))
b=int(input("Enter the breadth of the box: "))
h=int(input("Enter the height of the box: "))
vol=volume(l,b,h)
print("The volume of the box is: ",vol)