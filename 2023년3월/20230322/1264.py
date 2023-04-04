while True:
    count = 0
    n = input()
    if n =='#':
        break
    n = n.lower()
    for i in n:
        if i == 'a' or i =='e' or i == 'i' or i =='o' or i =='u':
            count += 1
    print(count)