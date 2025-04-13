from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dq=deque([entrance])
        visited[entrance[0]][entrance[1]] = True
        cnt=0
        dy=[0,0,1,-1]
        dx=[1,-1,0,0]
        while dq:
            size=len(dq)
            for _ in range(size):
                y,x=dq.popleft()
                if (y == 0 or x == 0 or y == len(maze)- 1 or x == len(maze[0]) - 1) and [y, x] != entrance:
                    return cnt
                for i in range(4):
                    ny=y+dy[i]
                    nx=x+dx[i]
                    if ny<0 or nx<0 or ny>=len(maze) or nx>=len(maze[0]): 
                        continue
                    if visited[ny][nx] or maze[ny][nx]=='+': 
                        continue
                    dq.append([ny,nx])  
                    visited[ny][nx]=True
            cnt+=1  
        return -1            
