# right sided triangle = decreasing space + increasing star
'''
          *
        * *
      * * *
    * * * *
  * * * * *
'''
n = int(input("enter number: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


for i in range(n):
    for j in range(n-i):
        print(" ",end = " ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()