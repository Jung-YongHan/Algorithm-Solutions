def solution(nums):
    poket = dict()
    for num in nums:
        poket[num] = poket.get(num, 0) + 1
    return min(len(nums)//2, len(poket.keys()))

# ������ Ǯ�� -> min�� set�Լ��� ����Ͽ� �����ϰ� Ǯ��
def solution(nums):
    return min(len(nums)//2, len(set(nums)))