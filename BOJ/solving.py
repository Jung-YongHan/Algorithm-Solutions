s = input().split('-')
result = []
for i in s:
    result.append(eval(i))
print(result[0]-sum(result[1:]))