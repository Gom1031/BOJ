s = input()
alphabet = [0]*26

for i in s:
    alphabet[ord(i)-97] += 1

print(' '.join(map(str,alphabet)))
