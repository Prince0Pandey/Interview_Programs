str = input("enter a word: ")
# reverse = ""
# lst = list(str)
# for i in range(len(lst),0,-1):
#     reverse += lst[i-1]
#
# if reverse == str:
#     print("palindrome string")
# else:
#     print("not palindrome string")

if str[::-1] == str:
    print("palindrome string")
else:
    print("not palindrome string")