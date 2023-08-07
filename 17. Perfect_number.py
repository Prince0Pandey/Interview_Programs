def perfect_number(number):
    sum = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            sum = sum + i

    if sum == number:
        print(f"Perfect number")
    else:
        print("not a perfect number")

n = int(input("enter number: "))
perfect_number(n)