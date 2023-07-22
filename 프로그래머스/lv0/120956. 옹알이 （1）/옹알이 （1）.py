from collections import deque
def solution(babbling):
    cnt = 0
    for i in babbling:
        stack = []
        d = deque(i)
        while d:
            a = d.popleft()
            stack.append(a)
            if ''.join(stack) == 'aya' or ''.join(stack) =='woo' or ''.join(stack) == 'ye' or ''.join(stack) == 'ma':
                stack = []
        if ''.join(stack) == '':
            cnt+=1
    return cnt