def solution(nums):
    poket = dict()
    for num in nums:
        if num in poket: 
            poket[num] += 1
        else: 
            poket[num] = 1
    answer = len(poket.keys())
    if answer > len(nums) // 2: 
        answer = len(nums) // 2
    return answer

# 간결한 풀이 -> min과 set함수를 사용하여 간결하게 풀이
def solution(nums):
    return min(len(nums)//2, len(set(nums)))