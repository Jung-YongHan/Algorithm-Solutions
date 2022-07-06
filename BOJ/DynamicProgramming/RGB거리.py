# 1149
import sys
input = sys.stdin.readline
n = int(input())
dp1, dp2, dp3 = [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(1, n+1):
    r, g, b = map(int, input().split())
    dp1[i] = min(r+dp2[i-1], r+dp3[i-1])
    dp2[i] = min(g+dp3[i-1], g+dp1[i-1])
    dp3[i] = min(b+dp1[i-1], b+dp2[i-1])
print(min(dp1[n], dp2[n], dp3[n]))

