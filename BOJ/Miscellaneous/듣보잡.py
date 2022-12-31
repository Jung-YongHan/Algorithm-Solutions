# 1764

import sys
n, m = map(int, input().split())
arr1 = set()
arr2 = set()
for i in range(n):
    arr1.add(sys.stdin.readline().rstrip())
for j in range(m):
    arr2.add(sys.stdin.readline().rstrip())
    
result = sorted(list(arr1 & arr2))
print(len(result))
for i in result:
    print(i)