# 11651

import sys

arr = []
n = int(input())
for _ in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:(x[1], x[0]))
for i in range(n):
    print(*arr[i])