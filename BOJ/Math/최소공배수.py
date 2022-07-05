# 최소공배수
t = int(input())
def gcd1(a, b): # b>a
    if b == 0:
        return a
    r = a % b
    return gcd1(b, r)
def gcd2(b, a): # a>b
    if a == 0:
        return b
    r = b % a
    return gcd2(a, r)
for i in range(t):
    x, y = map(int, input().split())
    if x > y:
        print(x * y // gcd2(x, y))
    elif x < y:
        print(x * y // gcd1(x, y))
    else:
        print(x)