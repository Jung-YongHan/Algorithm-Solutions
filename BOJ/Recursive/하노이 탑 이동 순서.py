def hanoi(a, b, k):
    global count
    count += 1
    
    if k == 1:
        result.append((a, b))
        return

    hanoi(a, 6-a-b, k-1)
    result.append((a, b))
    hanoi(6-a-b, b, k-1)

n = int(input())
count = 0
result = []
hanoi(1, 3, n)
print(count)
for i in result:
    print(i[0], i[1])
