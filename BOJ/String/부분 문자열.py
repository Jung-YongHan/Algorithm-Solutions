# 16916
t=input()
p=input()

def compute_lps(p, lps):
    length = 0
    index = 1
    while index < len(p):
        if p[length] == p[index]:
            length += 1
            lps[index] = length
            index += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                index += 1


def kmp(t, p):
    n=len(t)
    m=len(p)

    lps = [0] * (m+1)
    compute_lps(p, lps)

    i=j=0
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == m:
                print(1)
                return
        else:
            if j > 0:
                j = lps[j- 1]
            else:
                i += 1
    print(0)

kmp(t, p)
