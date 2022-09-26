def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(completion)):
        last = False
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        last = True
    if last: answer = participant[-1]
    return answer