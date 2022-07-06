# 3273

import sys
n=int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
result = 0
start = 0
end = n-1
while start < end:
    if arr[start] + arr[end] > x:
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        result += 1
        start += 1
        end -= 1
print(result)