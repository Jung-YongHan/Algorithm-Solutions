# 피보나치 함수
import sys
input = sys.stdin.readline
result0 = [0] * 42
result1 = [0] * 42
result0[0] = result1[1] = result0[2] = result0[3] = result1[2] = 1
result1[3] = 2
for i in range(int(input())):
    n = int(input())
    def fibo(n):

        if n <= 3:
            print(result0[n], result1[n])
            return
        for i in range(4, n+1):
            result0[i] = result0[i-1] + result0[i-2]
            result1[i] = result1[i-1] + result1[i-2]
        print(result0[n], result1[n])
        return
    fibo(n)