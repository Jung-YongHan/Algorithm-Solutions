# 2667
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input())))

result = []
count = 0
def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    if array[x][y] == 1:
        global count
        count += 1
        array[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)

