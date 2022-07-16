def func(x, y, z):
    if z == 1:
        graph[x][y] = '*'
        return
    n = z//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            func(x+n*i, y+n*j, n)
            
n = int(input())
graph = [[' ']*n for _ in range(n)]
func(0, 0, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()
