'''
* * * * *
* * * *
* * *
* *
*
'''
n = int(input("Enter Number: "))
for i in range(n):
    for j in range(i,n):            # (n-i)
        print("*", end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print(j+1, end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print(i, end=" ")
    print()