n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
visited = [False]*n
result = set()
def func(k):
    if k == m:
        print(*arr); return
    tmp = 0
    for i in range(n):
        # 이전 항의 마지막 값과 새로 들어온 항의 마지막 값이 같으면 중복
        if not visited[i] and tmp != nums[i]:
            arr[k] = nums[i]
            visited[i] = True
            tmp = arr[k]
            func(k+1)
            visited[i] = False
func(0)


# 내가 푼 풀이
# 결과 값을 set에 add시켜 중복을 제거
# 각 원소 값들은 순서*값에 해당하는 인덱스에 방문 여부를 저장
# 정렬되어 있으므로 위 값이 중복되는 경우는 없음
# n, m = map(int, input().split())
# nums = sorted(list(map(int, input().split())))
# arr = [0]*m
# visited = [False]*int(1e6)
# result = set()
# def func(k):
#     if k == m:
#         result.add(tuple(arr)); return
#     for i in range(len(nums)):
#         if not visited[i*nums[i]]:
#             arr[k] = nums[i]
#             visited[i*nums[i]] = True
#             func(k+1)
#             visited[i*nums[i]] = False
# func(0)
# for i in sorted(result):
#     for j in range(len(i)):
#         print(i[j], end=' ')
#     print()

