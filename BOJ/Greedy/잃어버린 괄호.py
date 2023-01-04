# 1541
s = input().split('-')
result = []
for i in s:
    result.append(sum(map(int, i.split('+'))))
print(result[0]-sum(result[1:]))
            

    