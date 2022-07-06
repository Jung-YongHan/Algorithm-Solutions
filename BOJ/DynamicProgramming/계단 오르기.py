import sys
input = sys.stdin.readline
n=int(input())
arr = []
for i in range(1, n+1):
    arr.append(int(input()))
dp = [0]*n
dp[0] = arr[0]
dp[1] = max(arr[1] + arr[0], arr[1])
dp[2] = max(arr[2] + arr[1], arr[2] + arr[0])
for i in range(3, n):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
print(dp[n-1])