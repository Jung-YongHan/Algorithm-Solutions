# ��ƼĿ�� ���� �� �ִ� ���� ���� �� �̶�� ���� ���ʿ� ��ġ.
# ���ʿ� �ش��ϴ� ��ġ�� ���� �� �̶�� ���߿��� ���� ������ ��ġ�� ����.
# ù��° Ǯ�� - �׽�Ʈ���̽��� ��� ����, ���� ���ڸ��� 'Ʋ�Ƚ��ϴ�'
# �Խ����� Ȯ���� ��� -> ȸ���� �ʹ� ������ ������ 1��, 2�� ������ ��������.
# => ȸ���� ��� ��ǥ�� ���� ���� �� ���� ���°� �Ǿ��� ���� �Ѵ�.
# �ι�° Ǯ�� -> ����.

n, m, k = map(int, input().split())
stickers = []
for i in range(k):
    a, _ = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(a)])

note = [[0]*m for _ in range(n)] # ��Ʈ��

# ��ƼĿ�� ȸ���ϴ� �Լ�
def rotate(sticker)->list:
    row, col = len(sticker), len(sticker[0])
    rotate_sticker = [[] for _ in range(col)]
    for j in range(col):
        for i in range(row-1, -1, -1):
            rotate_sticker[j].append(sticker[i][j])
    return rotate_sticker

# ��ƼĿ�� ���� �� �ִ��� Ȯ���ϴ� �Լ�
def is_avl(sticker): 
    if oob(sticker, 0, 0) and oob(rotate(sticker), 0, 0): # ũ�Ⱑ �Ѿ�� ��ƼĿ���� ����
        return False, _, _, _
    
    row, col = len(sticker), len(sticker[0])
    count = 0
    while count < 4:
        for i in range(n):
            for j in range(m):
                if check(sticker, i, j):
                    return True, sticker, i, j
        sticker = rotate(sticker)
        count += 1
    return False, _, _, _
            
# ��Ʈ�ϰ� ��ƼĿ�� ��ġ�� ���(�Ѵ� 1�� ��쿡�� False)
def check(sticker, x, y):
    if oob(sticker, x, y): # ������ ��� ��� False
        return False
    row, col = len(sticker), len(sticker[0])
    for a in range(row):
        for b in range(col):
            if note[x+a][y+b] == 1 and sticker[a][b] == 1:
                return False
    return True    

# ���� ��ǥ���� ��ƼĿ�� ��Ʈ���� ��踦 �Ѿ���� ���� �ľ�    
def oob(sticker, x, y)->bool: # out-of-bound
    row, col = len(sticker), len(sticker[0])
    if row+x > n or col+y > m: # ȸ�� ��
        return True
    return False

# ��ƼĿ�� ���̴� �Լ�
def attach(sticker, x, y):
    row, col = len(sticker), len(sticker[0])
    for i in range(row):
        for j in range(col):
            if note[x+i][y+j] == 1: 
                continue
            else:
                note[x+i][y+j] = sticker[i][j]

# ��ƼĿ�� ���� �� �ִ� ��ġ�� ����
for t in range(k):
    avl, stick, i, j = is_avl(stickers[t])
    if avl:
        attach(stick, i, j)

cnt = 0
for i in range(n):
    for j in range(m):
        if note[i][j] == 1:
            cnt += 1
print(cnt)