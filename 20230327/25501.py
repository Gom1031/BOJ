def recursion(s, l, r):
    global count
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        count += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

count = 1

T = int(input())

n = []
m = []

for i in range(T):
    n.append(input())
for i in n:
    m.append([isPalindrome(i), count])
    count = 1
for i in m:
    print(*i)