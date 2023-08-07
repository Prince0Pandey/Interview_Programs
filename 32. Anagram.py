string1 = input("enter first string: ")
string2 = input("enter second string: ")
if len(string1) == len(string2):
    for i in string1:
        if i in string2:
            pass
        else:
            print(f"{string1} & {string2} are not anagram.")
            break
    print(f"{string1} & {string2} are anagram.")
else:
    print(f"{string1} & {string2} are not anagram.")