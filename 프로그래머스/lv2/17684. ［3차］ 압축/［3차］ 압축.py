from collections import deque
def solution(msg):
    li = [[1,'A'],[2,'B'],[3,'C'],[4,'D'],[5,'E'],[6,'F'],[7,'G'],[8,'H'],[9,'I'],[10,'J'],[11,'K'],[12,'L'],[13,'M'],[14,'N'],[15,'O'],[16,'P'],[17,'Q'],[18,'R'],[19,'S'],[20,'T'],[21,'U'],[22,'V'],[23,'W'],[24,'X'],[25,'Y'],[26,'Z']]
    num = 27
    di = dict(li)
    ans = []
    q = deque(msg)
    s = q.popleft()
    while len(q)>0:
        c = q.popleft()
        if s+c in di.values():
            s+=c
        else:
            ans.append([key for key, value in di.items() if value == s][0])     
            di[num] = s+c
            s = c
            num+=1
    ans.append([key for key, value in di.items() if value == s][0])
    return ans