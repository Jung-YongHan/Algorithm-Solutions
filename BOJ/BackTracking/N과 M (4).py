n, m = map(int, input().split())
arr = [0]*m
def func(k):
    if k == m:
        print(*arr); return
    
    start = arr[k-1]
    if k == 0:
        start = 1
    for i in range(start, n+1):
        arr[k] = i
        func(k+1)
func(0)