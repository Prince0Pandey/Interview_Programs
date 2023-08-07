# right sided triangle = increasing space + decreasing star
'''
  * * * * *
    * * * *
      * * *
        * *
          *
'''
n = int(input("Enter number:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(n-i):
        print(j+1,end=" ")
    print()