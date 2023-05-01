n = int(input())

# 딕셔너리 생성
count = {}

for _ in range(n):
    name = input()
    first = name[0]
    
    # 딕셔너리에 있으면 key값 +1, 없으면 1로 설정
    if first in count:
        count[first] += 1
    else:
        count[first] = 1

team = []

# print(count) 


# for루프에서는 dic자료형을 반복할수없음
# .items 메서드를 사용하여 dic자료형을 반복하도록 만듦
# letter, cnt 변수에 for 루프로 값 할당
for letter, cnt in count.items():
    if cnt >= 5:
        team.append(letter)

if team:
    team.sort()
    print(''.join(team))
else:
    print("PREDAJA")
