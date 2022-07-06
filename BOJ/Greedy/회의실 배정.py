# 1931
# 회의실의 최대 개수를 찾는 문제
# 회의는 중간에 중단X, 끝남과 동시에 시작 가능, 시작시간과 끝나는 시간이 같을 수 있음
# 이 문제의 핵심이다.
# 끝나는 시간을 오름차순 정렬, 시작하는 시간을 오름차순을 정렬해야 함
import sys

n = int(input())
time = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    time.append((a, b))
time.sort(key=lambda x:(x[1], x[0]))

count, end = 0, 0
for s, e in time:
    if s >= end:
        count += 1
        end = e
print(count)