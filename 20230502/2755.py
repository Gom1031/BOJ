import sys

n = int(sys.stdin.readline())
m =  [list(sys.stdin.readline().split()) for _ in range(n)]

result = 0
chong_hakjum = 0

for i in range(n):
    hakjum = int(m[i][1])
    chong_hakjum += hakjum
    if m[i][2] == 'A+':
        sungjuk = 4.3
    elif m[i][2] == 'A0':
        sungjuk = 4.0
    elif m[i][2] == 'A-':
        sungjuk = 3.7
    elif m[i][2] == 'B+':
        sungjuk = 3.3
    elif m[i][2] == 'B0':
        sungjuk = 3.0
    elif m[i][2] == 'B-':
        sungjuk = 2.7
    elif m[i][2] == 'C+':
        sungjuk = 2.3
    elif m[i][2] == 'C0':
        sungjuk = 2.0
    elif m[i][2] == 'C-':
        sungjuk = 1.7
    elif m[i][2] == 'D+':
        sungjuk = 1.3
    elif m[i][2] == 'D0':
        sungjuk = 1.0
    elif m[i][2] == 'D-':
        sungjuk = 0.7
    elif m[i][2] == 'F':
        sungjuk = 0

    result += sungjuk * hakjum 

print("%.2f" % (round(result/chong_hakjum + 10**-10, 2)))