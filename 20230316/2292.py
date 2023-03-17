n = int(input())
num_list = [[1],[2,3,4,5,6]]

if n < 7:
    index = num_list.index(n)
    print(index)

x = 12
while True:
    for i in range(1,x+1):
        new_list = []
        new_list.append(i)
        num_list.append(new_list)
        x += 6

print(num_list)