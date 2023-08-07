number = temp = int(input("enter integer number: "))
octal = ""
while temp > 0:
    remainder = temp % 8
    octal = str(remainder) + octal
    temp = temp//8
print(f"octal number of {number} is {octal}")