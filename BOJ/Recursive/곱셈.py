a, b, c = map(int, input().split())

def find(a, b, c):
    if b == 1:
        return a%c
    temp = find(a, b//2, c)
    temp = temp * temp % c
    if b%2 == 0:
        return temp
    return temp * a%c

print(find(a, b, c))