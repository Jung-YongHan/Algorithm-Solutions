import sys

n, m = map(int, input().split())
arr1 = set()
arr2 = list()
for i in range(n+m):
    s = sys.stdin.readline().rstrip()
    if s in arr1:
        arr2.append(s)
    else:
        arr1.add(s)
arr2.sort()
print(len(arr2))
for i in arr2:
    print(i)