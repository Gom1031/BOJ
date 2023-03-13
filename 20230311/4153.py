while True:
    num = list(map(int, input().split()))
    max_num = num.pop(num.index(max(num)))
    if sum(num) == 0:
        break
    if num[0] ** 2 + num[1] ** 2 == max_num ** 2:
        print('right')
    else:
        print('wrong')