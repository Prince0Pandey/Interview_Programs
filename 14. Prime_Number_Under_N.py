rang = int(input("enter range: "))
lst = []
number = 2
flag = True
if rang > 0:
    while number <= rang:
        for i in range(2,number//2+1):
            flag = True
            if number%i == 0:
                flag = False
                break
        if flag:
            lst.append(number)
        number = number + 1
else:
    print("Invalid range")
print(f"Prime Numbers under {rang} are: {lst}")