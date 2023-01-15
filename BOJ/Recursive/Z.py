def solve(x, y, n): # 2^n x 2^n 배열에서 (r,c)를 방문하는 순서를 반환
    if n == 0:
        return 0
    half = 2**(n-1)
    if x < half and y < half: # 1번 사각형
        return solve(x, y, n-1)
    elif x < half and y >= half:
        return half*half + solve(x, y-half, n-1)
    elif x >= half and y < half:
        return 2*half*half + solve(x-half, y, n-1)
    else:
        return 3*half*half + solve(x-half, y-half, n-1)

n, r, c = map(int, input().split())
print(solve(r, c, n))