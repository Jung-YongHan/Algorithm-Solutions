# 스티커를 붙일 수 있는 곳이 여러 곳 이라면 가장 위쪽에 위치.
# 위쪽에 해당하는 위치도 여러 곳 이라면 그중에서 가장 왼쪽의 위치를 선택.
# 첫번째 풀이 - 테스트케이스는 모두 정답, 제출 하자마자 '틀렸습니다'
# 게시판을 확인한 결과 -> 회전에 너무 집중한 나머지 1번, 2번 과정을 무시했음.
# => 회전은 모든 좌표를 돌고 붙일 수 없는 상태가 되었을 때만 한다.
# 두번째 풀이 -> 성공.

n, m, k = map(int, input().split())
stickers = []
for i in range(k):
    a, _ = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(a)])

note = [[0]*m for _ in range(n)] # 노트북

# 스티커를 회전하는 함수
def rotate(sticker)->list:
    row, col = len(sticker), len(sticker[0])
    rotate_sticker = [[] for _ in range(col)]
    for j in range(col):
        for i in range(row-1, -1, -1):
            rotate_sticker[j].append(sticker[i][j])
    return rotate_sticker

# 스티커를 붙일 수 있는지 확인하는 함수
def is_avl(sticker): 
    if oob(sticker, 0, 0) and oob(rotate(sticker), 0, 0): # 크기가 넘어가는 스티커들은 배제
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
            
# 노트북과 스티커가 겹치는 경우(둘다 1인 경우에만 False)
def check(sticker, x, y):
    if oob(sticker, x, y): # 범위를 벗어난 경우 False
        return False
    row, col = len(sticker), len(sticker[0])
    for a in range(row):
        for b in range(col):
            if note[x+a][y+b] == 1 and sticker[a][b] == 1:
                return False
    return True    

# 현재 좌표에서 스티커가 노트북의 경계를 넘어가는지 유무 파악    
def oob(sticker, x, y)->bool: # out-of-bound
    row, col = len(sticker), len(sticker[0])
    if row+x > n or col+y > m: # 회전 전
        return True
    return False

# 스티커를 붙이는 함수
def attach(sticker, x, y):
    row, col = len(sticker), len(sticker[0])
    for i in range(row):
        for j in range(col):
            if note[x+i][y+j] == 1: 
                continue
            else:
                note[x+i][y+j] = sticker[i][j]

# 스티커를 붙일 수 있는 위치에 부착
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