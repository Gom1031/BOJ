n = int(input())
stack = [] # 스택 생성
result = [] # 결과를 저장할 리스트 생성
count = 1 # 스택에 쌓을 숫자

for i in range(1, n+1):
    data = int(input())
    while count <= data: # 입력된 숫자까지 스택에 쌓기
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == data: # 입력된 숫자가 스택의 가장 위에 있으면 꺼내기
        stack.pop()
        result.append("-")
    else: # 수열을 만들 수 없는 경우
        print("NO")
        exit(0)

print('\n'.join(result)) # 결과 출력