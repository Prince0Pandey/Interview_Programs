'''
*
* *
* * *
* * * *
* * * * *
'''
n = int(input("Enter Number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()