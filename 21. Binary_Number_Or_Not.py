# My Approach
'''
number = input("Enter number: ")
lst = list(number)
lst1 = []
flag = True
for digit in lst:
    digit = int(digit)
    lst1.append(digit)
    if digit == 0 or digit ==1:
        pass
    else:
        flag = False
        break
if flag:
    print(f"{number} is binary number")

else:
    print(f"{number} is not binary number")
'''


num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary")
