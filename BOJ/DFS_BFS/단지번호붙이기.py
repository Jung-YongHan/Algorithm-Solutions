# 2667
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                count += 1
                dfs(nx, ny)
            
    
result = []
count = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            dfs(x, y)
            result.append(count+1)
            count = 0

print(len(result))
for i in sorted(result):
    print(i)

