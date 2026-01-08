# logical operators example

x = int(input("Enter a number: "))
if x > 0 and x % 2 == 0:
    print(f"{x} is a positive even number.")
else:
    print(f"{x} is either not positive or not even.")