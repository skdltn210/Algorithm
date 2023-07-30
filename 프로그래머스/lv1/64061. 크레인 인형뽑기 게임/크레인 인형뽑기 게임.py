def solution(board, moves):
    cnt = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1]=0
                if len(stack)>=2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt+=2
                break
    return cnt