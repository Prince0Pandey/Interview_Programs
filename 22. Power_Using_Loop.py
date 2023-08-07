base = int(input("enter base: "))
power = int(input("enter power: "))
pow = 1

# for i in range(power):
#     pow = pow * base
# print(f"Value = {pow}",end="")

number = 1
while number <= power:
    pow = pow * base
    number += 1
print(f"Value = {pow}", end="")
