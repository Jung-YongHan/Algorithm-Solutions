# 1946
# �������� �׸��� ������ ���İ� �ð��ʰ��� ����� 1��for���� ����� ����
# 2��for���� ������� �ʱ� ���� ���������� ���� �ð��� ����
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[0])
    
    result = 1
    hire = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < hire:
            hire = arr[i][1]
            result += 1
    print(result)

