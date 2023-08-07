# Hill Pattern = decreasing space + Increasing star + Increasing star with 1 less star
'''
TYPE 1
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
'''

n = int(input("Enter number:"))
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()