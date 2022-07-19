n, m = map(int, input().split())
arr = [0]*m
def func(k, st):
    if k == m:
        print(*arr); return
    if k == 0:
        st = 1
    for i in range(st, n+1):
        arr[k] = i
        func(k+1, i)
func(0, 0)