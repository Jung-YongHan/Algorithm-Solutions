# 18111

import sys
input = sys.stdin.readline

# 세로 n, 가로 m, 맨 왼쪽 위의 좌표 (0, 0), 집터 내의 땅의 높이를 일정하게 바꾸기
n, m, b = map(int, input().split())
INF = int(1e9)
arr = []
for _ in range(n):
    for i in map(int, input().split()):
        arr.append(i)
arr.sort()
min_val, max_val = arr[0], arr[-1]
result = []
for i in range(min_val, max_val+1):
    need_b, avl_b, tmp_t = 0, 0, 0
    for j in arr:
        if j < i:    
            tmp_b = i - j  # 쌓기 위한 블록 수
            tmp_t += tmp_b         # 필요한 시간
            need_b += tmp_b
        elif j > i:
            tmp_b = j - i   # 인벤토리에 넣어지는 블록 수
            tmp_t += 2*tmp_b        # 필요한 시간
            avl_b += tmp_b

    if b + avl_b - need_b < 0:
        result.append((INF, -1))
    else:
        result.append((tmp_t, i))

result.sort(key=lambda x:(x[0], -x[1]))
print(result[0][0], result[0][1])