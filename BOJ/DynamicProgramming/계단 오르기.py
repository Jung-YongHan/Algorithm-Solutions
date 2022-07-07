# 2579
import sys

input = sys.stdin.readline
n=int(input())
arr = [0] * 301
dp = [0] * 301

for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = max(arr[1] + arr[0], arr[1])
dp[2] = max(arr[2] + arr[1], arr[2] + arr[0])
for i in range(3, n):
    dp[i] = arr[i]+ max(dp[i-2], dp[i-3]+arr[i-1])
print(dp[n-1])