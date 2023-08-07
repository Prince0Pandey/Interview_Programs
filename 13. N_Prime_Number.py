no_of_prime_number = int(input("enter range: "))
lst = []
number = 2
flag = True
if no_of_prime_number >= 0:
    while len(lst) < no_of_prime_number:
        for i in range(2, number // 2 + 1):
            flag = True
            if number % i == 0:
                flag = False
                break
        if flag:
            lst.append(number)
        number = number + 1
    print(f"{no_of_prime_number} Prime number: {lst}", end="")
else:
    print("Invalid range")