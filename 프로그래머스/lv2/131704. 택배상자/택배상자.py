from collections import deque
def solution(order):
    d = deque([i for i in range(1,len(order)+1)])
    o = deque(order)
    stack = []
    cnt = 0
    while True:
        if len(d)!=0 and d[0]==o[0]:
            d.popleft()
            o.popleft()
            cnt+=1
        elif len(stack)!=0 and stack[-1]==o[0]:
            stack.pop()
            o.popleft()
            cnt+=1
        else:
            if len(d) != 0:
                stack.append(d.popleft())
            else:
                return cnt