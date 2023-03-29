while True:
    n = str(input())

    if n == '.':
        break
    
    stack = []

    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                print("no")
                break
            last = stack.pop()
            if (i == ')' and last != '(') or (i == ']' and last != '['):
                print("no")
                break
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
        continue