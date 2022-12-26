for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            arr[j] += arr[j-1]
    print(arr[-1])