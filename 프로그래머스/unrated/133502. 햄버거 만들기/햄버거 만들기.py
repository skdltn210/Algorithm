def solution(ingredient):
    stack = []
    cnt = 0
    for i in ingredient:
        x = i
        stack.append(x)
        if len(stack)>=4 and stack[-4]==1 and stack[-3]==2 and stack[-2]==3 and stack[-1]==1:
            cnt+=1
            for i in range(4):
                stack.pop()
    return cnt