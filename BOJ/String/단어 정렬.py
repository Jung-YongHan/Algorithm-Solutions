# 1181

import sys
input = sys.stdin.readline

arr = set()
for i in range(int(input())):
    arr.add(input())

arr = list(arr)
t = len(arr)
for i in range(t):
    tmp1 = list(arr[i])
    tmp2 = []
    for j in range(len(tmp1)):
        tmp2.append(str(ord(tmp1[j])+3))
    arr[i] = "".join(tmp2)
arr.sort(key=lambda x:(len(x), int(x)))

for i in range(t):
    tmp = []
    val = arr[i]
    for j in range(len(val)//3):
        num = int(val[j*3:j*3+3])
        tmp.append(chr(num-3)) 
    print("".join(tmp))