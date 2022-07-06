# 5430
from collections import deque

for i in range(int(input())):
    command = input()
    size = int(input())
    
    nums = input()[1:-1].split(',')
    q = deque()
    for j in range(size):
        q.append(nums[j])
        
    result = 0
    r_count = 0
    for k in command:
        if k == 'R':
            r_count += 1
        else:
            if r_count % 2 == 0:
                if q:
                    q.popleft()
                else:
                    result = -1
                    break
            else:
                if q:
                    q.pop()
                else:
                    result = -1
                    break

    if r_count % 2 != 0:
        q.reverse()
    if result == 0:
        print('['+','.join(q)+']')
    else:
        print('error')