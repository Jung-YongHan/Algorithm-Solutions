# 6064

import sys
input = sys.stdin.readline
def solve(m, n, x, y):
    k = x
    while k <= m*n:
        if (k-x)%m==0 and (k-y)%n==0:
            return k
        k += m # k는 m을 더해주어도 x와 같음
    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))