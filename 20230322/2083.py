people = []
out = []
while True:
    command = list(input().split())
    people.append(command)
    if people.pop() == ['#', '0', '0']:
        break
    else:
        people.append(command)

for i in people:
    if int(i[1]) > 17 or int(i[2]) > 80:
        outin = [i[0], 'Senior']
        out.append(outin)
        # out.append(list(i[0], 'Senior'))
    else:
        outin = [i[0], 'Junior']
        out.append(outin)
        # out.append(list(i[0], 'Junior'))
for i in out:
    print(*i)