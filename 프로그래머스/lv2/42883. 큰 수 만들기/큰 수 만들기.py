from collections import deque
def solution(number, k):
    number = deque(number)
    q = deque()
    flag = 0
    while k>0 and len(number)>0 :
        if len(q) == 0:
            q.append(number.popleft())
        if q[-1]<number[0]:
            flag = 1
            q.pop()
            k-=1
        else:
            q.append(number.popleft())
    if flag == 0:
        for i in range(k):
            q.pop()
    return ''.join(list(q)) + ''.join(list(number))
