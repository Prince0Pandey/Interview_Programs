# using main function
'''
def main():
    n = int(input("enter number: "))
    ans = is_palindrome(n)
    print(ans)
def is_palindrome(number):
    temp = number
    reverse = 0
    while temp != 0:
        remainder = temp % 10
        reverse = reverse * 10 + remainder
        temp = temp // 10
    return f"{number} is palindrome number" if reverse == number else f"{number} is not palindrome number"

main()
'''
number = int(input("enter a number: "))
temp = number
reverse = 0
while temp != 0:
    remainder = temp % 10
    reverse = reverse * 10 + remainder
    temp = temp // 10

if reverse == number:
    print(f"{number} is palindrome number")

else:
    print(f"{number} is not palindrome number")
