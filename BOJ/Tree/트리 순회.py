# 1991
# 기본적인 트리 순회 문제

# 첫번째 풀이
# 클래스를 사용하지 않고 각각 문자의 아스키코드를 변환 후
# 리스트의 인덱스를 숫자로 사용, 재귀를 이용해 순환해 주었음.
def preorder(trees, root):
    print(chr(root+64), end='')
    if trees[root][0] != -1:
        preorder(trees, trees[root][0])
    if trees[root][1] != -1:
        preorder(trees, trees[root][1])
    return

def inorder(trees, root):
    if trees[root][0] != -1:
        inorder(trees, trees[root][0])
    print(chr(root+64), end='')
    if trees[root][1] != -1:
        inorder(trees, trees[root][1])
    return

def postorder(trees, root):
    if trees[root][0] != -1:
        postorder(trees, trees[root][0])
    if trees[root][1] != -1:
        postorder(trees, trees[root][1])
    print(chr(root+64), end='')
    return

n = int(input())
trees = [[] for _ in range(n+1)]
for _ in range(n):
    tmp = list(input().split())
    for i in range(3):
        if tmp[i] == '.':
            tmp[i] = -1
        else:
            tmp[i] = ord(tmp[i]) - 64
    trees[tmp[0]] = [tmp[1], tmp[2]]

preorder(trees, 1)
print()
inorder(trees, 1)
print()
postorder(trees, 1)

#////////////////////////////////////////////////////////////////////

# 두번째 풀이(참고)
# 트리를 사전으로 간단하게 관계만 표현. 간결한 코드
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')