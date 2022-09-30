from copy import deepcopy
# out of bounds Ȯ��
def oob(x, y):
    if 0 <= x < n and 0 <= y < m:
        return False
    return True

# (x, y)���� dir �������� �����ϸ鼭 ���� ���� �� ���� ����ġ�� ��� ��ĭ�� 7�� �ٲٴ� �Լ�
def upd(x, y, dir):
    dir = int(dir % 4)
    while True:
        x += dx[dir]
        y += dy[dir]
        if oob(x, y) or board2[x][y] == 6: # ������ ����ų� ���� ���� ���
            return
        if board2[x][y] != 0: # �ش� ĭ�� ��ĭ�� �ƴ� ���(cctv�� ���� ���)
            continue
        board2[x][y] = 7

# ����, ����, ����, ���� ����
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
mn = 0 # �簢 ������ �ּ� ũ��

board1 = [list(map(int, input().split())) for _ in range(n)] # ���ʿ� �Է¹��� board�� ������ ����Ʈ
board2 = [] # �簢 ������ ������ ���� ���� ����� ����
cctv =[]
for i in range(n):
    for j in range(m):
        if board1[i][j] != 0 and board1[i][j] != 6:
            cctv.append((i, j))
        if board1[i][j] == 0:
            mn += 1

# tmp�� 4�������� ���� �� �� �ڸ����� cctv�� �������� ������ ���̴�.
for tmp in range(4**len(cctv)):
    board2 = deepcopy(board1)
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4 # 4�����̹Ƿ� 4�� ���� �������� �̿��� �ڸ��� ����
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