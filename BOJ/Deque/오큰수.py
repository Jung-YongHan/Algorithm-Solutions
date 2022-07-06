# 17298
n = int(input())
array = list(map(int, input().split()))
st = []
result = [-1] * n
for i in range(n):
    if st:
        if st[-1][0] >= array[i]:
            st.append((array[i], i))
        else:
            for j in range(len(st)-1, -1, -1):
                if array[i] > st[j][0]:
                    a = st.pop()
                    result[a[1]] = array[i]
                else:
                    break
            st.append((array[i], i))
    else:
        st.append((array[i], i))
print(*result)