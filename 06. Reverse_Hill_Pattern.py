# Reverse Hill Pattern = Increasing Spaces + decreasing star + decreasing star (with 1 less star)
'''
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
'''
n = int(input("engter number: "))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print()