'''MY APPROCH
n = 1234
temp = n
count = 1
while temp//10 != 0:
    temp = temp//10
    count = count*10

reverse = 0
while n%10 != 0:           #2356
    remainder = n%10
    reverse = reverse + remainder*count
    count = count//10
    n = n // 10

print(reverse)
'''

# using while loop
'''
n = int(input("Please give a number: "))
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10
    n = n//10
print(f"reversed number: {reverse}")
'''

# using string slicing
'''
num = int(input("Please give a number: "))
rev = int(str(num)[::-1])
print("After reverse the number:", rev)
'''

# using recursion
def reverse(num):
    if num < 10:
        return num
    else:
        return (num % 10) * 10**(len(str(num))-1) + reverse(num // 10)

num = int(input("Please enter a number: "))
rev = reverse(num)
print("After reverse the number:", rev)