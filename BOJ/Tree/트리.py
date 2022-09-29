# 1068
# dfs�� �̿��ϸ� ����ġ��� ���� ����
# �׽�Ʈ���̽��� �������� �پ��Ͽ� ����ó�� �ϱⰡ ��ٷο���.
def remove_node(root):
    tree[root] = -2
    for i in range(n):
        if tree[i] == root:
            tree[i] = -2
            remove_node(i)

n = int(input())
tree = list(map(int, input().split()))
remove = int(input())

remove_node(remove)
count = 0
for i in range(n):
    if tree[i] != -2:
        is_avl = True
        for j in tree: # i��尡 -2�� �ƴϸ鼭 
            if i == j: # �ڽ��� �θ���� ���� �ʴ´ٸ�
                is_avl = False
                break
        if is_avl:
            count+=1
print(count)

# 20line�� -2�� �ƴ϶�� ��Ʈ����̰ų� ������� �Ǵ� 
# �ڽĳ�带 ���� �� �ִ� �θ����̴�.
# ���� ��Ʈ���ų� �ڽĳ�尡 �ִ� �θ����� ������尡 �ƴϹǷ� ���� �߰� X
# �ڽ��� �θ���� �����ʴ� -> ��������� ���� �߰����־���.