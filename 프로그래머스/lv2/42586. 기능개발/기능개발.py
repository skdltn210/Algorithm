from collections import deque

def solution(progresses, speeds):
    ans = []
    dqp = deque(progresses)
    dqs = deque(speeds)
    while len(dqp)>0:
        cnt=0
        while len(dqp)>0 and dqp[0]>=100:
            dqp.popleft()
            dqs.popleft()
            cnt+=1
        if cnt>0:
            ans.append(cnt)
        for i in range(len(dqp)):
            dqp[i] += dqs[i]
    return ans