# 한번 입은 옷들의 조합을 절대 다시 안입는다
# 알몸이 아닌 상태로 며칠 돌아다닐수있는가
# 테스트케이스 t
# 첫째줄에는 가진 의상 n
# 의상의 이름과 종류가 공백으로

t = int(input())

for _ in range(t):
    n = int(input())
    weardict = {}
    for _ in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)