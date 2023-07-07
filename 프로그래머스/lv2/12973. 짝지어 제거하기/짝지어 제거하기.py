def solution(s): 
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if stack[len(stack)-1] == stack[len(stack)-2] and len(stack)>1:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0