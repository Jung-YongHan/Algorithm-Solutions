# 11729

k = int(input())

def func(a, b, n):
    if n == 1:
        print(a, b)
        return
    func(a, 6-a-b, n-1)
    print(a, b)
    func(6-a-b, b, n-1)

print((2**k)-1)
func(1, 3, k)