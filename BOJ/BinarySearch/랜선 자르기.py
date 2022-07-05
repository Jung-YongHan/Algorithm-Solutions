# 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
result = []
def bi(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    total = 0
    for i in arr:
        total += i // mid

    if total >= target:
        result.append(mid)
        return bi(arr, target, mid+1, end)
    else:
        return bi(arr, target, start, mid-1)
bi(arr, n, 1, max(arr))
print(max(result))
