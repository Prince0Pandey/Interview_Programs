n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter third number: "))

if n1>n2 and n1>n3:
    print(f"{n1} is greatest")

elif n2>n1 and n2>n3:
    print(f"{n2} is greatest")

else:
    print(f"{n3} is greatest")