# 10814

import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().split())
arr.sort(key=lambda x:(int(x[0])))
for i in range(n):
    print(*arr[i])