        # MY Approach #

# string = input("enter string: ")
# character = input("input character to remove from string: ")
# if character in string:
#     print(string.replace(character,''))
# else:
#     print(f"character is not in a string:")


# The translate() method in python returns a string where some specified characters are replaced
# with the character described in a dictionary, or in a mapping table.
# ord() function which takes a character as an input and convert it to ascii.
string = input("enter string: ")
character = input("input character to remove from string: ")
dict = {ord(character) : None}          # instead of none we can write any thing ex. "" or "triangle"
print(string.translate(dict))
