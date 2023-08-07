#my approach
'''
n = input("enter numbers: ").split(',')
lst = list(n)
div = len(lst)
sum = 0
for i in lst:
    sum = sum + int(i)
avg = sum/div
print(f"average: {avg}")
'''

rang = int(input("number of elements: "))
lst = []

for i in range(1,rang+1):
    element = int(input(f"enter {i} number: "))
    lst.append(element)
avg = sum(lst)/rang
print(f"Average of {rang} numbers: {avg}")