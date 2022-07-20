graph = [list(map(int, input().split())) for _ in range(9)]
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
square = [[[False]*3 for _ in range(3)] for _ in range(10)]

for i in range(9):
    for j in range(9):
        val = graph[i][j]
        if val != 0:
            row[i][val] = True
            col[j][val] = True
            square[val][i//3][j//3] = True

def solve(x, y):
    if x == 9 and y == 8:
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=' ')
            print()
        exit()
    
    if x == 9:
        x = 0 
        y += 1

    if graph[x][y] == 0:
        for num in range(1, 10):
            if not square[num][x//3][y//3] and not row[x][num] and not col[y][num]:
                graph[x][y] = num
                square[num][x//3][y//3] = True
                row[x][num] = True
                col[y][num] = True
                solve(x+1, y)
                graph[x][y] = 0
                row[x][num] = False
                col[y][num] = False
                square[num][x//3][y//3] = False
    else:
        solve(x+1, y)
    
solve(0, 0)
