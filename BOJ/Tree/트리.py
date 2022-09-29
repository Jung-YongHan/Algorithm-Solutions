# 1068
# dfs를 이용하면 가지치기는 쉬운 문제
# 테스트케이스가 생각보다 다양하여 예외처리 하기가 까다로웠다.
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
        for j in tree: # i노드가 -2가 아니면서 
            if i == j: # 자신을 부모노드로 갖지 않는다면
                is_avl = False
                break
        if is_avl:
            count+=1
print(count)

# 20line은 -2가 아니라면 루트노드이거나 리프노드 또는 
# 자식노드를 가질 수 있는 부모노드이다.
# 만일 루트노드거나 자식노드가 있는 부모노드라면 리프노드가 아니므로 개수 추가 X
# 자신을 부모노드로 갖지않는 -> 리프노드라면 개수 추가해주었다.