        # MY APPROACH #
# string = input("enter string: ")
# character = input("enter character: ")
# occurence = 0
# for i in string:
#     if i == character:
#         occurence = occurence + 1
#
# print(f"Occurence of '{character}' in '{string}': {occurence}")

string = input("Please enter String : ")
character = input("Please enter a Character : ")
index, occurence = 0, 0
while(index < len(string)):
    if string[index] == character:
        occurence = occurence + 1
    index = index + 1
print(f"Occurence of '{character}' in '{string}': {occurence}")