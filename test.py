dic = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
n = int(input()) #과목 수
grade = []
score = []

for i in range(1, n+1):
    sub_scr_grd = input().split()
    score.append(int(sub_scr_grd[1]))
    grade.append(dic[sub_scr_grd[2]])
# print(score)
# print(grade)
for i in range(0, n):
    result = score[i]*grade[i]
    print(result)