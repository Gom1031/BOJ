import sys

t = int(sys.stdin.readline())
for i in range(t):
    test = list(map(int, sys.stdin.readline().split()))
    k = test.pop(0)
    test.sort()
    result = 0
    for j in range(len(test)-1):
        result = max(result, test[j+1] - test[j])
    print("Class %d" %(i+1))
    print("Max %d, Min %d, Largest gap %d" %(test[k-1], test[0], result))