# 17478

n = int(input())
s = n
q1 = '"재귀함수가 뭔가요?"'
q2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
q3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
q4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
a1 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
a2 = '라고 답변하였지.'

dash = '____'

def func1(n):
    if n == s:
        return
    print(dash*n+q1); print(dash*n+q2); print(dash*n+q3); print(dash*n+q4)
    return func1(n+1)
    
def func2(n):
    if n == 0:
        return
    print(dash*(n-1)+a1)
    func2(n-1)

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
func1(0)
print(dash*n+q1)
print(dash*n+a1)
print(dash*n+a2)
func2(n)
