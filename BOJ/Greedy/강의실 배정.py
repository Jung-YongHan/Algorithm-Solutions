# 11000

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:(x[0], x[1]))

room = [arr[0]]
# for i in range(1, n):
#     # ���� ���� �������� �ٽ� Ǯ��
#     # if arr[i][0] == room[]
