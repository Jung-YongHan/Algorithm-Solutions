# 5397
import sys

def find_password(s1, s2, password):
    for c in password:
        if c == '<':
            if s1:
                s2.append(s1.pop())
        elif c == '>':
            if s2:
                s1.append(s2.pop())
        elif c == '-':
            if s1:
                s1.pop()
        else:
            s1.append(c)
    s1.extend(reversed(s2))
    return ''.join(s1)

for i in range(int(sys.stdin.readline().rstrip())):
    password = list(sys.stdin.readline().rstrip())
    s1 = []
    s2 = []
    result = find_password(s1, s2, password)
    print(result)
