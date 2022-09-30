from copy import deepcopy
# out of bounds 확인
def oob(x, y):
    if 0 <= x < n and 0 <= y < m:
        return False
    return True

# (x, y)에서 dir 방향으로 진행하면서 벽을 만날 때 까지 지나치는 모든 빈칸을 7로 바꾸는 함수
def upd(x, y, dir):
    dir = int(dir % 4)
    while True:
        x += dx[dir]
        y += dy[dir]
        if oob(x, y) or board2[x][y] == 6: # 범위를 벗어나거나 벽을 만난 경우
            return
        if board2[x][y] != 0: # 해당 칸이 빈칸이 아닐 경우(cctv가 있을 경우)
            continue
        board2[x][y] = 7

# 동쪽, 남쪽, 서쪽, 북쪽 순서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
mn = 0 # 사각 지대의 최소 크기

board1 = [list(map(int, input().split())) for _ in range(n)] # 최초에 입력받은 board를 저장할 리스트
board2 = [] # 사각 지대의 개수를 세기 위해 사용할 변수
cctv =[]
for i in range(n):
    for j in range(m):
        if board1[i][j] != 0 and board1[i][j] != 6:
            cctv.append((i, j))
        if board1[i][j] == 0:
            mn += 1

# tmp를 4진법으로 뒀을 때 각 자리수를 cctv의 방향으로 생각할 것이다.
for tmp in range(4**len(cctv)):
    board2 = deepcopy(board1)
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4 # 4진법이므로 4로 나눈 나머지를 이용해 자리수 도출
        brute /= 4
        x, y = cctv[i]
        if board1[x][y] == 1:
            upd(x, y, dir)
        elif board1[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir+2)
        elif board1[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir+1)
        elif board1[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
        else:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
            upd(x, y, dir+3)
    val = 0
    for i in range(n):
        for j in range(m):
            if board2[i][j] == 0:
                val += 1
    mn = min(mn, val)

print(mn)