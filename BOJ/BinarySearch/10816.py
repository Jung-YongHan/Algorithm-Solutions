# 숫자 카드
n=int(input())
cards = sorted(list(map(int, input().split())))

m=int(input())
result = list(map(int, input().split()))


def bin(cards, card, low, high):
    if low > high:
        return
    mid = (low + high) // 2
    if cards[mid] == card:
        del cards[mid]
        return 1
    elif cards[mid] > card:
        return bin(cards, card, low, mid - 1)
    else:
        return bin(cards, card, mid + 1, high)

answer = [0] * m
for i in range(m):
    while True:
        if bin(cards, result[i], 0, len(cards)-1) == 1:
            answer[i] += 1
        else:
            break

print(*answer)