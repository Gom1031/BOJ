def is_right(s):
    stack = 0
    for c in s:
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
            if stack < 0:
                return False
    return stack == 0


def generate_brackets(s, pos):
    if pos == len(s):
        if is_right(s):
            return ''.join(s)
        else:
            return None

    if s[pos] == 'G':
        s[pos] = '('
        result = generate_brackets(s, pos + 1)
        if result is not None:
            return result

        s[pos] = ')'
        result = generate_brackets(s, pos + 1)
        if result is not None:
            return result

        s[pos] = 'G'
    else:
        result = generate_brackets(s, pos + 1)
        if result is not None:
            return result

    return None


n = int(input())
s = list(input().strip())
result = generate_brackets(s, 0)
print(result)
