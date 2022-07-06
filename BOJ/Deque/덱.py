# 10866
import sys
n = int(sys.stdin.readline())
count = 0
dequeue = []
for i in range(n):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'push_front':
        dequeue.insert(0, int(command[1]))
        count += 1
    elif command[0] == 'push_back':
        dequeue.append(int(command[1]))
        count += 1
    elif command[0] == 'pop_front':
        if dequeue:
            print(dequeue[0])
            del dequeue[0]
            count -= 1
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dequeue:
            print(dequeue[-1])
            del dequeue[-1]
            count -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(count)
    elif command[0] == 'empty':
        print(1) if count == 0 else print(0)
    elif command[0] == 'front':
        print(dequeue[0]) if dequeue else print(-1)
    else:
        print(dequeue[-1]) if dequeue else print(-1)