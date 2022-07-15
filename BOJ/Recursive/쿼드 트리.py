def isValid(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[x][y] != graph[i][j]:
                return False
    return True

def solve(x, y, n):
    if isValid(x, y, n):
        print(graph[x][y], end='')
        return 
    
    half = n // 2
    print('(', end='')
    for i in range(2):
        for j in range(2):
            solve(x+i*half, y+j*half, half)
    print(')', end='')

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
solve(0, 0, n)
