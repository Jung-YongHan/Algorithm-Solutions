import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    print(*arr[i])