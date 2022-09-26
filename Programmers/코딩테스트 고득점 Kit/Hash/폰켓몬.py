def solution(nums):
    poket = dict()
    for num in nums:
        poket[num] = poket.get(num, 0) + 1
    return min(len(nums)//2, len(poket.keys()))

# 간결한 풀이 -> min과 set함수를 사용하여 간결하게 풀이
def solution(nums):
    return min(len(nums)//2, len(set(nums)))