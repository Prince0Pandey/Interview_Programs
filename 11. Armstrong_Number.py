# My approach
'''
n = int(input("enter number: "))
temp = n
sum = 0
lenght = len(str(n))
while temp != 0:
    remainder = temp%10
    sum = sum + remainder**lenght
    temp = temp//10

if sum == n:
    print("armstrong number")

else:
    print("not armstrong number")
'''
# Armstrong number using list comprehension
num = int(input("Please Enter a Number: "))
digits = [int(digit) for digit in str(num)]
count = len(digits)
sum = sum([digit ** count for digit in digits])
if num == sum:
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not a armstrong number")