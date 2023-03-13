repeat = int(input())
char = []
for i in range(repeat):
    char.append(input())
char = list(set(char))
char.sort()
char.sort(key=len)

for i in range(len(char)):
    print(char[i])