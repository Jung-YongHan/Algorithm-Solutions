# 백준 베르트랑 공준
m = []
while True:
    t = int(input())
    if t==0:
        break
    m.append(t)

def prime(n):
    arr = [k for k in range(0, n*2+1)]
    count = 0
    for i in range(2, n*2+1):
        if arr[i]==0:
            continue
        j=i*2
        while j <= n*2:
            arr[j]=0
            j+=i
    for k in range(n+1, 2*n+1):
        if arr[k]!=0 and arr[k]!=1:
            count+=1
    print(count)

for j in range(len(m)):
    prime(m[j])
