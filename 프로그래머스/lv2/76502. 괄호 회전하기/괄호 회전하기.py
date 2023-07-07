def solution(s):
    cnt = 0
    for j in range(len(s)):
        lst = []
        for i in range(len(s)):
            lst.append(s[i])
            if len(lst) >= 2:
                if lst[-1] == ']' and lst[-2] == '[':
                    lst.pop()
                    lst.pop()
                elif lst[-1] == ')' and lst[-2] == '(':
                    lst.pop()
                    lst.pop()
                elif lst[-1] == '}' and lst[-2] == '{':
                    lst.pop()
                    lst.pop()
        if len(lst) == 0:
            cnt += 1
        s = s[1:] + s[0:1]
    return cnt
    