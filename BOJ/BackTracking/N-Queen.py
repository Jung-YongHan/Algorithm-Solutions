n = int(input())
isused1 = [False]*n
isused2 = [False]*(2*n-1)
isused3 = [False]*(2*n-1)
result = 0
def func(k):
    global result
    if k == n:
        result += 1
        return
    for i in range(n):
        if not isused1[i] and not isused2[k+i] and not isused3[k-i+n-1]:
            isused1[i] = True
            isused2[k+i] = True
            isused3[k-i+n-1] = True
            func(k+1)
            isused1[i] = False
            isused2[k+i] = False
            isused3[k-i+n-1] = False
func(0)
print(result)

# n = int(input())
# graph = [[False]*n for _ in range(n)]
# result = 0

# def solve(k):
#     global result
#     if k == n:
#         result += 1
#         return
#     for i in range(n):
#         if ud(k, i) and diagnol(k, i):
#             graph[k][i] = True
#             solve(k+1)
#             graph[k][i] = False

# 상하를 확인하고 대각선을 확인하는 방법은 풀 수는 있으나, O(n^2)이 지속적으로 발생 => 시간초과
# # 상하 확인
# dy1 = [-1, 1]
# def ud(x, y):
#     for i in range(2):
#         ny = y + dy1[i]
#         while 0 <= ny < n:
#             if graph[x][ny]:
#                 return False
#             ny += dy1[i]
#     return True

# # 대각선 확인
# dx2 = [-1, -1, 1, 1]
# dy2 = [1, -1, 1, -1]
# def diagnol(x, y):
#     for i in range(4):
#         nx = x + dx2[i]
#         ny = y + dy2[i]
#         while 0 <= nx < n and 0 <= ny < n:
#             if graph[nx][ny]:
#                 return False
#             nx += dx2[i]
#             ny += dy2[i]
#     return True

