from collections import deque
def solution(x, y, n):
    visited = [0] * 1000001
    def bfs(x,y,n):
        q = deque()
        visited[x] = 1
        q.append(x)
        while q:
            x = q.popleft()
            if 0 <= x+n <= 1000000 and visited[x+n] == 0:
                visited[x+n] = visited[x]+1
                q.append(x+n)
            if 0 <= x*2 <= 1000000 and visited[x*2] == 0:
                visited[x*2] = visited[x]+1
                q.append(x*2)
            if 0 <= x*3 <= 1000000 and visited[x*3] == 0:
                visited[x*3] = visited[x]+1
                q.append(x*3)
    bfs(x,y,n)
    return visited[y]-1
            