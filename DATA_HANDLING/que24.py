P=int(input("Enter the value of P:"))
R=float(input("Enter the value of R:"))
T=int(input("Enter the value of T:"))
CI=P*(1+R/100)**T
print("Compound Interest is:",CI)
print("Total payable amount is:",CI+P,"rupees")