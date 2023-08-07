n = [8,88,56,7,0,34,65,88,56,7,23]
for i in range(len(n)):
    for j in range(len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
print(n)
