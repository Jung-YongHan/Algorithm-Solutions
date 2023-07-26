# 7662

from heapq import heappush, heappop
import sys

for _ in range(int(input())):
    visited = [False] * 1_000_001
    q_min = []
    q_max = []

    for key in range(int(input())):
        oper = sys.stdin.readline().split()
        if oper[0] == 'I':
            heappush(q_min, (int(oper[1]), key))
            heappush(q_max, (-int(oper[1]), key))
            visited[key] = True

        elif oper[1] == '1':
            while q_max and not visited[q_max[0][1]]: 
                heappop(q_max)                        
            if q_max:
                visited[q_max[0][1]] = False
                heappop(q_max)

        else:
            while q_min and not visited[q_min[0][1]]:
                heappop(q_min)
            if q_min:
                visited[q_min[0][1]] = False
                heappop(q_min)
    
    while q_min and not visited[q_min[0][1]]:
        heappop(q_min)
    while q_max and not visited[q_max[0][1]]:
        heappop(q_max)
    
    print(-q_max[0][0], q_min[0][0]) if q_max and q_min else print('EMPTY')