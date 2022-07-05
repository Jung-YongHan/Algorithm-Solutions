# 숫자 카드
from bisect import bisect_left, bisect_right

n=int(input())
cards = sorted(list(map(int, input().split())))
m=int(input())
array = list(map(int, input().split()))

def find(arr, x):
    left = bisect_left(arr, x)
    right = bisect_right(arr, x)
    return right - left

result = []
for i in array:
    result.append(find(cards, i))

print(*result)