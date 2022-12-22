# 첫번째 풀이 - 예제는 모두 정답
def check(a, x, y):
    chess = [row[y:y+8] for row in a[x:x+8]]
    change = 0
    for i in range(8):
        change += abs(chess[i].count("B") - chess[i].count("W")) // 2
    return change

m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(input()))

result = []
for i in range(m-7):
    for j in range(n-7):
        result.append(check(arr, i, j))
print(min(result))

# 두번째 풀이 - 반례 확인, 체스를 만들고 비교 후 개수 확인 (정답)
def check(a, x, y):
    chess = [row[y:y+8] for row in a[x:x+8]]
    
    board1, board2 = make_board()
    
    change1 = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != board1[i][j]:
                change1 += 1
    
    change2 = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != board2[i][j]:
                change2 += 1

    return min(change1, change2)

def make_board():
    row1 = 'BWBWBWBW'
    row2 = 'WBWBWBWB'
    board1 = []
    board2 = []
    for _ in range(4):
        board1.append(list(row1))
        board1.append(list(row2))

    for _ in range(4):
        board2.append(list(row2))
        board2.append(list(row1))

    return board1, board2

m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(input()))

result = []
for i in range(m-7):
    for j in range(n-7):
        result.append(check(arr, i, j))
print(min(result))

# 세번째 풀이 - 다른 풀이 참고
def check(board, x, y):
    chess = [row[y:y+8] for row in board[x:x+8]]
    
    change1, change2 = 0, 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if chess[i][j] != 'W':
                    change1 += 1
                if chess[i][j] != 'B':
                    change2 += 1
            else:
                if chess[i][j] != 'B':
                    change1 += 1
                if chess[i][j] != 'W':
                    change2 += 1

    return min(change1, change2)

m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(input()))

result = []
for i in range(m-7):
    for j in range(n-7):
        result.append(check(arr, i, j))
print(min(result))