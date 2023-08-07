def factorial(num):
    fact = 1
    if num >= 0:
        while num > 0:
            fact = num*fact
            num-=1
    else:
        print("invalid number")
    return fact
n = int(input("enter number: "))
print(factorial(n))


