from collections import deque
def solution(n, computers):
    visited = []
    q=deque()
    cnt = 0
    
    for i in range(n):
        if i not in visited:
            q.append(i)
            cnt+=1
            while q:
                a = q.popleft()
                for i in range(n):
                    if i not in visited and computers[a][i] == 1:
                        visited.append(i)
                        q.append(i)
    return cnt       