import sys

jay = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

if len(jay) >= len(doctor):
    print("go")
else:
    print("no")
