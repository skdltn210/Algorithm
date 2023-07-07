def solution(cards):
    arr = []
    visited = [ 0 for i in range(len(cards))]
    cnt = 0
    
    def visit(x):
        nonlocal cnt
        if visited[x] == 1:
            return 
        else:
            cnt+=1
            visited[x] = 1
            if 0 <= cards[x-1] < len(cards): 
                visit(cards[x-1])
    
    for i in range(len(cards)):
        cnt = 0
        visit(i)
        arr.append(cnt)
        if 0 not in visited:
            break
    arr.sort(reverse = True)
    if len(arr) < 2:
        return 0
    return arr[0] * arr[1]    