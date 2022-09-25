# 11000

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:(x[0], x[1]))

room = [arr[0]]
# for i in range(1, n):
#     # 강의 개수 지정부터 다시 풀기
#     # if arr[i][0] == room[]
