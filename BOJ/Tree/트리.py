# 1068
# https://77dptjd.tistory.com/13 참고하여 다시 풀기 22.09.29
def remove_node(root):
    if tree[root] != [None]:
        values = tree[root]
        for i in values:
            remove_node(i)
            del tree[i]

n = int(input())
tree = {}
tmp = [[] for _ in range(n)]
for i, root in enumerate(list(map(int, input().split()))):
    if root != -1:
        tmp[root].append(i)

for i in range(n):
    if tmp[i]:
        tree[i] = tmp[i]
    else:
        tree[i] = [None]

remove = int(input())
if remove == 0:
    del tree
    print(0)
else:
    remove_node(remove) # 가지치기
    del tree[remove] # 해당 노드도 제거

    cnt = 0
    for key in tree.keys():
        if tree[key] != [None]:
            leaf = False
            for value in tree[key]:
                if value in tree:
                    leaf = False
                    break
                else:
                    leaf = True
            if leaf:
                tree[key] = [None]
    for key in tree.keys():
        if tree[key] == [None]:
            cnt += 1
    print(cnt)