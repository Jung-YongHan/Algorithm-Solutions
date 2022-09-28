# 1043
# set자료구조의 강력함을 알 수 있는 문제
# 진실을 아는 사람과 함께 있는 사람을 union해주는 방식
# 순서에 영향이 있는 문제이기 때문에 각각의 파티를 m번씩 돌아주었다.
n, m = map(int, input().split())
known = set(map(int, input().split()[1:]))

party = []
for i in range(m):
    party.append(set(map(int, input().split()[1:])))

result = [True]*m
for _ in range(m):
    for i, p in enumerate(party):
        if known & p:
            result[i] = False
            known |= p
print(result.count(True))