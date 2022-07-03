# 쇠막대기
s = input()
st = []
result = 0
for i in range(len(s)):
    if s[i] == '(':
        st.append(s[i])
    else:
        if s[i-1] == '(':
            st.pop()
            result += len(st)
        else:
            st.pop()
            result += 1
print(result)