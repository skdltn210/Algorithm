from collections import deque
def solution(m, n, board):
    cnt = 0
    board = [list(x) for x in board]
    q = deque()
    while True:
        flag = 0
        for i in range(m-1):
            for j in range(n-1):
                if not board[i][j] == 'X' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    if not [i,j] in q:
                        q.append([i,j])
                    if not [i,j+1] in q:
                        q.append([i,j+1])
                    if not [i+1,j] in q:
                        q.append([i+1,j])
                    if not [i+1,j+1] in q:
                        q.append([i+1,j+1])
                    flag = 1
        if flag==0:
            return cnt
        cnt+=len(q)
        while q:
            y, x = q.popleft()
            board[y][x] = 'X'
        for x in range(n):
            x_cnt = 0
            for y in range(m-1,-1,-1):
                if board[y][x] == 'X':
                    x_cnt+=1
                else:
                    q.append(board[y][x])
            for i in range(x_cnt):
                q.append('X')
            for y in range(m-1,-1,-1):
                board[y][x] = q.popleft()