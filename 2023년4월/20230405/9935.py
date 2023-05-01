import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

left = []

for char in string:
    left.append(char)
    if len(left) >= len(bomb) and ''.join(left[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            left.pop()

print("".join(left) if left else "FRULA")
