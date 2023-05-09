import random

row, col = (4, 4) #row = 세로 / col = 가로
puzzle = [] #광역 변수 (밖에 있기 때문에 함수에서 사용할 수 있음)

def rand_puzzle():
    arr= [i for i in range(row*col)]
    arr= random.sample(arr, row*col)

    for i in range(0, len(arr), col):
        puzzle.append(arr[i:i+col])

def prt_puzzle():
    for i in range(row):
        for j in range(col):
            if puzzle[i][j] != 0:
                print("%4s" %puzzle[i][j], end='')
            else:
                print("%4s" %'', end='')
        print() #들여쓰기

def find_zero():
    for i in range(row):
        for j in range(col):
            if puzzle[i][j] == 0:
                return i, j #0의 행, 열 값
def left(r, c):
    if c-1 >= 0:
            puzzle[r][c], puzzle[r][c+1] = puzzle[r][c+1], puzzle[r][c]
def right(r, c):
    if c-1 >= 0:
            puzzle[r][c], puzzle[r][c-1] = puzzle[r][c-1], puzzle[r][c]
def up(r, c):
    if r+1 < row:
            puzzle[r][c], puzzle[r+1][c] = puzzle[r+1][c], puzzle[r][c]
def down(r, c):
    if r-1 >= 0:
            puzzle[r][c], puzzle[r-1][c] = puzzle[r-1][c], puzzle[r][c]

rand_puzzle()
prt_puzzle()
while True:
    r, c = find_zero()
    key = input("a(좌)w(상)s(하) d(우) > ")
    if key == "a": #Left
        left(r, c)
    elif key == "d": #Right
        right(r, c)
    elif key == "w":#Up
        up(r, c)
    elif key == "s":#Down
        down(r, c)
    elif key == "0":
        print("End")
        break
    else:
        print("??잘못된키값입니다!")
    prt_puzzle()
# print(prt_puzzle)