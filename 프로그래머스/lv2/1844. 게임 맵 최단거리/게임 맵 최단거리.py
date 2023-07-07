from collections import deque
def solution(maps):
    x_max = len(maps)
    y_max = len(maps[0])
    visited = [[0]*y_max for i in range(x_max)]
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    visited[0][0]=1
    q = deque([(0,0)])
    
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<x_max and 0<=nx<y_max:
                if visited[ny][nx] == 0 and maps[ny][nx]==1:
                    visited[ny][nx] = visited[y][x]+1
                    q.append((ny,nx))
    if visited[x_max-1][y_max-1] == 0:
        return -1
    else:
        return visited[x_max-1][y_max-1]