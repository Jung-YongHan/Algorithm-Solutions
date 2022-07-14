# 2217
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort(reverse=True)

maximum = 0
for i in range(n):
    maximum = max(maximum, array[i]*(i+1))
print(maximum)