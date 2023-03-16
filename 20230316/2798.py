n, m = map(int,input().split())
num_list = list(map(int,input().split()))

sum_list = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = num_list[i]+num_list[j]+num_list[k]
            sum_list.append(sum)
sum_list = set(sum_list)

# print(sum_list)

if m in sum_list:
    print(m)
else:
    for i in range(m+1):
        m -= 1
        if m in sum_list:
            print(m)
            break