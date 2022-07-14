# 1780

n = int(input())
result = [0]*3
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 내부 숫자가 모드 같은지 확인하는 함수
def valid(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[x][y] != graph[i][j]:
                return False
    return True

def solve(x, y, z):
    if valid(x,y,z):
        result[graph[x][y]+1] += 1
        return
    
    n = z//3
    for i in range(3):
        for j in range(3):
            solve(x+n*i, y+n*j, n)
    
solve(0, 0, n)
for i in result:
    print(i)