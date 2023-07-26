n = int(input())
m = int(input())
s = input()
start, end = 0, 1
count = 0
result = 0
while end < m:
    # start 포인터가 I를 가르킬 때까지 이동
    if s[start] == 'O':
        start += 1
        end += 1
    else:
        # end 포인터가 가르키는 값과 이전 값이 같은 경우 하나씩 증가 ex) II
        if s[end] == s[end-1]:
            start += 1
            end += 1
        else:
            # 교차하는 경우 교차 카운트 1 증가 및 end point 이동
            count += 1
            # 교차 횟수가 n의 2배일 시 문자열이 속한 것이므로 개수 증가 및 start 이동, end start+1로 이동
            if count == 2*n:
                result += 1
                count = 0
                start += 1
                end = start+1
            else:
                end += 1
print(result)