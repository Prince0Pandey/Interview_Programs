        # My Approach #
# lst1 = [2,3,4,2,6,7,3,2,4,7,3,2,4,6]
# lst2 = []
# count = 0
# while count < len(lst1):
#     if lst1[count] in lst2:
#         pass
#     else:
#         lst2.append(lst1[count])
#     count += 1
# print(f"Original list: {lst1}")
# print(f"Without duplicate list: {lst2}")

lst1 = [2,3,4,2,7,3,6,2,4,7,3,2,4,6]
lst2 = []
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print(f"Original list: {lst1}")
print(f"Without duplicate list: {lst2}")
