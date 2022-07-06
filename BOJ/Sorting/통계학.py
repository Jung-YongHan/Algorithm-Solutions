# 2018
import sys
from collections import Counter
n = int(input())
nums = []
sum = 0
for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    sum += num    
nums.sort()
print(round(sum/n))
print(nums[n//2])

count = Counter(nums).most_common()
if len(count) > 1:
    if count[1][1] == count[0][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(nums[-1] - nums[0])

