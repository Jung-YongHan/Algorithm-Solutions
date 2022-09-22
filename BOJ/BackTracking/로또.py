# 6603
# 중복없이 오름차순으로 숫자를 나열하는 전형적인 백트레킹 문제
while True:
    tc = list(map(int, input().split()))
    k = tc[0]
    if k == 0:
        break
    s = tc[1:]
    arr = [0]*6
    def func(k, st):
        if k == 6:
            print(*arr); return
        else:
            for i in range(st, len(s)):
                arr[k] = s[i]
                func(k+1, i+1)
    func(0, 0)
    print()