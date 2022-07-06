# 11659

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum = [0] * (len(nums) + 1)
for i in range(1, len(nums)+1):
    sum[i] = sum[i-1] + nums[i-1]

for j in range(m):
    v, w = map(int, input().split())
    print(sum[w] - sum[v-1])
