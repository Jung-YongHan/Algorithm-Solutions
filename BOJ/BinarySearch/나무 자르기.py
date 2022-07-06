# 2805
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += i-mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
