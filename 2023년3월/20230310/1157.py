c = list(input())

#대문자로 변환
for i in range(len(c)):
    c[i] =c[i].upper()

uc = list(set(c))

cnt_list = []
for x in uc:
    cnt = c.count(x)
    cnt_list.append(cnt)

#최대값이 중복되면 ?
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(uc[max_index])