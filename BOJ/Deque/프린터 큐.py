# 1966
from collections import deque
n=int(input())
c = deque()
maximum = 0
for i in range(n): # a는 문서의 개수, b는 몇 번째로 인쇄 궁금, c는 문서의 중요도 리스트
    order = 0
    a, b = map(int, input().split())
    t = list(map(int, input().split()))
    for j in range(len(t)):
        c.append(t[j])
    while len(c) > 0:
        maximum = max(c)
        if b != 0:  # b를 확인할 차례가 아닌 경우
            if c[0] >= maximum:
                c.popleft()
                order += 1
            else:
                c.append(c.popleft())
            b -= 1
        else:
            if c[0] >= maximum:
                order += 1
                print(order)
                break
            else:
                b = len(c)-1
                c.append(c.popleft())
    c.clear()

