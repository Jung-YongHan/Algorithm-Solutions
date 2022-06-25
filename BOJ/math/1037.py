# 약수
# N을 N의 가장 작은 약수로 나누면 N의 가장 큰 약수가 나오는 것을 이용
m = int(input())
n = list(map(int, input().split()))
min_num = 1e7
max_num = 1
for i in range(len(n)):
    if n[i] > max_num:
        max_num = n[i]
    if n[i] < min_num:
        min_num = n[i]
print(min_num*max_num)
