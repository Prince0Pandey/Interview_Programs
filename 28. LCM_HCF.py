n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

        # LCM OF A NUMBER #
# if n1 < 0 and n2 < 0:
#     n1 = -n1
#     n2 = -n2
#     greater = max(n1, n2)
#     while True:
#         if greater % n1 == 0 and greater % n2 == 0:
#             break
#         greater += 1
#     print(f"LCM of {-n1} and {-n2}: {-greater}")
#
# else:
#     greater = max(n1, n2)
#     while True:
#         if greater % n1 == 0 and greater % n2 == 0:
#             break
#         greater += 1
#     print(f"LCM of {n1} and {n2}: {greater}")

        # HCF or GCD OF A NUMBER #
smaller = min(n1,n2)
while True:
    if n1%smaller == 0 and n2%smaller == 0:
        break
    smaller = smaller - 1
print(f"HCF of {n1} and {n2}: {smaller}")
