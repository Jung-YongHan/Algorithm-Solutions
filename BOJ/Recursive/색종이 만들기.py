# 2630
def valid(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[x][y] != graph[i][j]:
                return False
    return True

def solve(x, y, n):
    if valid(x, y, n):
        result[graph[x][y]] += 1
        return

    half = n//2
    for i in range(2):
        for j in range(2):
            solve(x+i*half, y+j*half, half)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = [0]*2
solve(0, 0, n)
for i in result:
    print(i)