s = input()
k = s.find("x")
if k==-1:
    print(0)
elif k==0:
    print(1)
elif k==1 and s[0] == "-":
    print(-1)
else:
    print(s[:k])