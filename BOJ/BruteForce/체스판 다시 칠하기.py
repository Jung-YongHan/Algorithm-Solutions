# 체스판 다시 칠하기
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

def counter(subBoard):
    bcount = wcount = 0
    for v in range(8):
        for w in range(8):
            if subBoard[v][w] == 'B':
                bcount += 1
            else:
                wcount += 1
    if subBoard[0][0] == subBoard[7][7] and subBoard[7][0] == subBoard[0][7]:
        return abs(bcount - wcount)
    else:
        return 65

minimum = 65
for i in range((n+1)-8):
    for j in range((m+1)-8):
        subBoard = [row[j:j+8] for row in board[i:i+8]]
        minimum = min(minimum, counter(subBoard))

print(minimum//2)


