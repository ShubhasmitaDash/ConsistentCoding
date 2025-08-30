def d2r(amount, convert):
    rupee=amount*convert
    return rupee

con=int(input("Enter the conversion of 1 dollar to rupees:"))
dollar=int(input("Enter the dollars to be converted:"))
ru=d2r(dollar,con)
print(ru)

