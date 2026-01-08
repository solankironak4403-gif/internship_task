# simple intrest calculation
p = int(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter time in years: "))
si = (p * r * t) / 100
print(f"Simple Interest: {si}")