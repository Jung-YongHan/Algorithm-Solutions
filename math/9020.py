# 골드바흐의 추측
# 어떤 짝수가 두 소수의 합으로 구할 수 있다는 
import sys
t = int(sys.stdin.readline())
m = []
for _ in range(t):
    m.append(int(sys.stdin.readline()))

def goldbagh(n):
    arr = prime(n)
    result = []
    for i in range(n//2+1):
        if arr[i] == 0:
            continue
        if arr[n-i] + arr[i] == n:
            result.append((i, n-i))
    min_value = 10001
    min_index = 0
    for k in range(len(result)):
        distance = result[k][1] - result[k][0]
        if distance < min_value:
            min_value = distance
            min_index = k
    print(result[min_index][0], result[min_index][1])

def prime(n):
    arr = [k for k in range(n+1)]
    for i in range(2, n+1):
        if arr[i] == 0:
            continue
        j = i * 2
        while j <= n:
            arr[j] = 0
            j += i
    return arr

for i in range(t):
    goldbagh(m[i])

