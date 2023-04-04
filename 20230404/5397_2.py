import sys
n = int(input())

for _ in range(n):
    left_stack = list(sys.stdin.readline().rstrip())
    right_stack = []
    result = []
    
    for i in left_stack:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
                continue
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
                continue
        elif i == '-':
            if left_stack:
                left_stack.pop()
                continue
        else: 
            result.append(i)
    print(*result)