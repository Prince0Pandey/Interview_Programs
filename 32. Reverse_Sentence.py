        # MY APPROACH #
# word = input("enter a word: ")
# reverse = ""
# for i in range(len(word)-1,-1,-1):
#     reverse = reverse + word[i]
# print(reverse)

# print(word[::-1])

sentence = input("enter a sentence: ").split(" ")
reverse_sentence = " "
for i in sentence[::-1]:
    reverse_sentence = reverse_sentence + i[::-1] + " "
    #ecnetnes desrever si siht

print(reverse_sentence)