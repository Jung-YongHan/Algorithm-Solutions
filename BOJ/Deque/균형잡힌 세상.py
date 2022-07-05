# 균형잡힌 세상
import sys
input = sys.stdin.readline
while True:
    string = input()
    stack = []
    isValid = True
    if string[0] == '.':
        break
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                isValid = False
                break
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                isValid = False
                break
            stack.pop()
    if stack:
        isValid = False
    if isValid:
        print('yes')
    else:
        print('no')

