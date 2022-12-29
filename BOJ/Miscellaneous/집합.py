# 11723 집합

import sys

s = set()
for i in range(int(input())):
    command = sys.stdin.readline().split(" ")
    if command[0] == 'add':
        s.add(int(command[1]))
    elif command[0] == 'remove':
        s.discard(int(command[1]))
    elif command[0] == 'check':
        print(1) if int(command[1]) in s else print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == 'all':
        del s
        s = set(range(1, 21))
    else:
        s.clear()