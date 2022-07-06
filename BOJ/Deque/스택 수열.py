# 1874
import sys

n = int(sys.stdin.readline().rstrip())

s1 = [] # 수열
s2 = [] # push
s3 = [] # pop
for i in range(n):
    s1.append(int(sys.stdin.readline()))

nums = [x for x in range(n, 0, -1)]
num = 0 
index = 0
result = []
while index < n:
    if num != s1[index]:
        if nums:    
            s2.append(nums.pop())
            result.append('+')
            num = s2[-1]
        else:
            break
    else:
        if s2:
            s3.append(s2.pop())
            index += 1
            result.append('-')
            if s2:
                num = s2[-1]
            else:
                num = 0
    
if s2:
    print('NO')
else:
    for i in result:
        print(i)
    