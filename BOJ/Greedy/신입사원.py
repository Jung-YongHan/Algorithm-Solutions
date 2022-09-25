# 1946
# 전형적인 그리디 문제로 정렬과 시간초과를 고려한 1중for문을 사용한 문제
# 2중for문을 사용하지 않기 위해 변수지정을 통해 시간을 줄임
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[0])
    
    result = 1
    hire = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < hire:
            hire = arr[i][1]
            result += 1
    print(result)

