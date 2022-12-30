import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for i in range(n):
    arr.append(input().rstrip())

for _ in range(m):
    s = input().rstrip()
    if s.isdigit():
        print(arr[int(s)-1])
    else:
        print(arr.index(s)+1)