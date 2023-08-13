def solution(babbling):
    cnt=0
    for b in babbling:
        arr = ['aya','ye','woo','ma']
        stack = []
        word = ''
        for i in range(len(b)):
            stack.append(b[i])
            if ''.join(stack)==word:
                break
            if ''.join(stack) in arr:
                word = ''.join(stack)
                stack=[]
                
        if len(stack) == 0:
            cnt+=1
    return cnt