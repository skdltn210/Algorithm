def solution(board):
    cnt_o, cnt_x = 0, 0
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 'O':
                cnt_o += 1
            elif board[y][x] == 'X':
                cnt_x += 1
    
    if cnt_o != cnt_x and cnt_o != cnt_x + 1:
        return 0

    def is_winner(player):
        for i in range(3):
            if board[i][0] == player and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return True
            if board[0][i] == player and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

    o_wins = is_winner('O')
    x_wins = is_winner('X')

    if o_wins and x_wins:
        return 0
    if o_wins and cnt_o != cnt_x + 1:
        return 0
    if x_wins and cnt_o != cnt_x:
        return 0

    return 1