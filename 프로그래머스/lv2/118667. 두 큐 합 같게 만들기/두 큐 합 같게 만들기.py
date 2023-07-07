from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    if (sum(q1) + sum(q2))%2 == 1:
        return -1
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    cnt = 0
    while True:
        if q1_sum > q2_sum:
            a = q1.popleft()
            q2.append(a)
            q1_sum-=a
            q2_sum+=a
            cnt+=1
        elif q1_sum < q2_sum:
            b = q2.popleft()
            q1.append(b)
            q1_sum+=b
            q2_sum-=b
            cnt+=1
        else:
            break
        if cnt>300001:
            return -1
    return cnt