#My approach
# n = int(input("enter number to find square root: "))
# print(f"square of a number: {pow(n,0.5)}")

import math
#take input from the user
num = int(input("Enter a number to find square root : "))
#check if the input number is negative
if num<0:
    print("Negative numbers can't have square roots")
else:
    print("square roots = ",math.sqrt(num))