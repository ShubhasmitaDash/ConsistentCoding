import math

def series(a,b):
    c=math.ceil(b/4)
    if c == 0:
        c = 1

    numbers = []
    for i in range(a,b+1, c):
        numbers.append(i)
    return numbers

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

result_list = series(a,b)
print(f"The generated series is: {result_list}")