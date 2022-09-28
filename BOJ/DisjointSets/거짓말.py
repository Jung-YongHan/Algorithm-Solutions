# 1043
# set�ڷᱸ���� �������� �� �� �ִ� ����
# ������ �ƴ� ����� �Բ� �ִ� ����� union���ִ� ���
# ������ ������ �ִ� �����̱� ������ ������ ��Ƽ�� m���� �����־���.
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