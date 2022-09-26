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

# ������ Ǯ�� -> min�� set�Լ��� ����Ͽ� �����ϰ� Ǯ��
def solution(nums):
    return min(len(nums)//2, len(set(nums)))