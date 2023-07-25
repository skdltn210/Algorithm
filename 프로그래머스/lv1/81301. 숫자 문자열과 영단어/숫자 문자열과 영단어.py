from collections import deque
def solution(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    numm = ['zero','one','two','three','four','five','six','seven','eight','nine']
    li = []
    s = deque(s)
    arr = []
    while s:
        x = s.popleft()
        if x not in num:
            li.append(x)
            if ''.join(li) in numm:
                arr.append(str(numm.index(''.join(li))))
                li = []
        else:
            arr.append(x)
            li = []
    return int(''.join(arr))
    
    
        