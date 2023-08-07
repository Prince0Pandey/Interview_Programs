# TYPE 1). Diamond Pattern = Hill Pattern + Reverse Hill Pattern
# TYPE 2). Diamond Pattern = Pyramid Pattern + Reverse Pyramid Pattern
'''
Type 1
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
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
for i in range(n):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n-2):
        print("*", end=" ")
    print()

'''
type 2
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

for i in range(n):
    for j in range(i+1,n):
        print("",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i+1,n):
        print("*", end=" ")
    print()