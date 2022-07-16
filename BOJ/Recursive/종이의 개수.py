import sys
input = sys.stdin.readline

def isValid(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[x][y] != graph[i][j]:
                return False
    return True

def solve(x, y, z):
    if isValid(x, y, z):
        result[graph[x][y] + 1] += 1
        return

    n = z//3
    for i in range(3):
        for j in range(3):
            solve(x+i*n, y+j*n, n)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [0]*3
solve(0, 0, n)
for i in range(3):
    print(result[i])