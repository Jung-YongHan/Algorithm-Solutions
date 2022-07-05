# 1904
# python의 int형은 변수가 담고 있는 값의 크기에 따라 유동적으로 사용하는
# 메모리가 변하기 때문에 모듈로를 이용해서 수를 계속 작게 유지
n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])