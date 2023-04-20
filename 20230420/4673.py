def d(n):
    n = n + sum(map(int, str(n)))
    return n

not_self = set()
for i in range(1, 10001):
    not_self.add(d(i))

for j in range(1, 10001):
    if j not in not_self:
        print(j)