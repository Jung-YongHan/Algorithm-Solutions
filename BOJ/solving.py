n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

def solve(x, y, n): # 재귀 함수
    if check(x, y, n):
        print(arr[x][y], end="")
    else:
        print("(", end="")
        for i in range(2):
            for j in range(2):
                solve(x+i*n//2, y+j*n//2, n//2)
        print(")", end="")

def check(x, y, n): # 같은 숫자인지 확인하는 함수
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

solve(0, 0, n)