a = []
full = []
for i in range(1, 31):
    full.append(int(i))
for i in range(28):
    a.append(int(input()))
for i in range(28):
    full.remove(a[i])
for i in range(len(full)):
    print(full[i])