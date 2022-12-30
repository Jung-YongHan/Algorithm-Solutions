# 1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = dict()
for i in range(n):
    s = input().rstrip()
    arr[s], arr[str(i+1)] = str(i+1), s

for _ in range(m):
    print(arr[input().rstrip()])