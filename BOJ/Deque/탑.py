# 2493
n = int(input())
array = list(map(int, input().split()))
st = []
result = [0] * n
for i in range(n):
    while st:
        top, index = st[-1][0], st[-1][1]
        if top > array[i]:
            result[i] = index+1
            st.append((array[i], i))
            break
        else:
            st.pop()
    st.append((array[i], i))
print(*result)