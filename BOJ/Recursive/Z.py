def func(n, r, c):
    if n == 0: return 0
    half = 2**(n-1)
    if r < half and c < half: return func(r, c, n-1)
    elif r < half and c >= half: return half*half + func(r, c-half, n-1)
    elif r >= half and c < half: return 2*half*half + func(r-half, c, n-1)
    else: return 3*half*half + func(r-half, c-half, n-1)

N, r, c = map(int, input().split())
graph = [[0]*N for _ in range(N)]
print(func(N, r, c))