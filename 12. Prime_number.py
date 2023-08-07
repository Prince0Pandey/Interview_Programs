n = int(input("enter number: "))
count = True
for i in range(2,n//2):
    if n%i == 0:
        count = False
        break

if count:
    print("Prime Number")
else:
    print("not prime number")