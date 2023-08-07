        # BINARY TO DECIMAL #
# binary_number = bin(int(input("Enter an integer :")))
# print(binary_number)

decimal = temp = int(input("Please Enter a decimal number: "))
binary = ""
while temp > 0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2
print("Binary number for ", decimal, " is ", binary)

        # DECIMAL TO BINARY #

binary = temp = int(input("Please Enter a binary number: "))
decimal, i = 0, 0
while temp != 0:
    remainder = temp%10
    decimal = decimal + remainder*pow(2,i)
    temp = temp // 10
    i += 1
print("decimal number for ",binary,"is ",decimal)