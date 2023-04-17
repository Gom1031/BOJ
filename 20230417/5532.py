vacation = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0: #나머지가 0이면
    l_day = a//c #몫 = 일수
else: #나머지가 0이 아니면
    l_day = (a//c) + 1 #몫+1 = 일수

if b % d == 0:
    m_day = b//d
else:
    m_day = (b//d) + 1

day = max(l_day, m_day) #국어와 수학 날짜중 가장 오래걸리는 애를 찾고

print(vacation - day) #전체 일수에서 뺴주면 최대로 놀 수 있는 날이 출력됨