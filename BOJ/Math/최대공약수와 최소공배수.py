# 2609
n, m = map(int, input().split())
result1, result2 = [], []
# 최대공약수 : 각 수의 공통된 약수 중에서 최댓값
# 최소공배수 : 각 수의 공통된 배수 중에서 최솟값
def gcd(n, m):
    if n > m:
        for i in range(1, n+1):
            if n % i == 0:
                if m % i == 0:
                    result1.append(i)
    elif n < m:
        for i in range(1, m+1):
            if m % i == 0:
                if n % i == 0:
                    result1.append(i)
    else:
        result1.append(n)
    return result1[-1]

def lcm(n, m):
    if gcd(n,m) == 1:
        return n*m
    if n > m:
        for i in range(1, m+1):
            n *= i
            for j in range(2, n+1):
                if m * j == n:
                    m *= j
                    return m
                elif m * j > n:
                    n //= i
                    break
    elif n < m:
        for i in range(1, n+1):
            m *= i
            for j in range(2, m+1):
                if n * j == m:
                    n *= j
                    return m
                elif n * j > m:
                    m //= i
                    break
    else:
        return n

print(gcd(n,m))
print(lcm(n,m))