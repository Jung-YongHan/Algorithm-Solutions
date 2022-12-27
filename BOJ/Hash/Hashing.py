# 15829

n = int(input())
s = list(input())
alphabet = dict()
for i in range(1, 27):
    alphabet[chr(96+i)] = i
result = 0
for i in range(n):
    result += alphabet[s[i]]*(31**i)
print(result % 1234567891)