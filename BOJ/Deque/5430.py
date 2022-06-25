# AC
from collections import deque

t = int(input())
deq = deque()
for i in range(t):
    result = 0
    repR = 0
    func = str(input())
    length = int(input())
    num = input()
    nums = num[1:-1].split(',')
    for j in range(length):
        deq.append(int(nums[j]))
    for k in func:
        if k == 'R':
            repR += 1
        else:
            if repR % 2 == 0:
                if deq:
                    deq.popleft()
                else:
                    result = -1
                    break
            else:
                if deq:
                    deq.pop()
                else:
                    result = -1
                    break
    if repR % 2 != 0:
        deq.reverse()
    if result == 0:
        print('[', end='')
        for u in range(len(deq)):
            if u != len(deq) - 1:
                print(deq[u], end=',')
            else:
                print(f'{deq[u]}', end='')
        print(']')
    else:
        print('error')
    deq.clear()