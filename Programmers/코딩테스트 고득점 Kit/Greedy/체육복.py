def solution(n, lost, reserve):
    students = [True] * (n+1)
    delete = []
    for i in reserve:
        for j in lost:
            if i == j:
                delete.append(i)
    reserve = sorted([x for x in reserve if x not in delete])
    lost = sorted([x for x in lost if x not in delete])
    
    for i in lost:
        students[i] = False
    
    for i in reserve:
        valid = True
        for j in lost:
            if valid and not students[j]:
                if j == i-1 or j == i+1:
                    students[j] = True
                    valid = False     
    
    answer = 0
    for i in students[1:]:
        if i:
            answer += 1
    return answer

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))