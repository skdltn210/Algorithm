def is_balanced(p):
    num = 0
    for i in p:
        if i == '(':
            num += 1
        elif i == ')':
            num -= 1
        if num < 0:
            return False
    return num == 0

def solution(p):
    if p == '':
        return ''
    num = 0
    for i in range(len(p)):
        if p[i] == '(':
            num += 1
        elif p[i] == ')':
            num -= 1
        if num == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    if is_balanced(u):
        return u + solution(v)
    
    else:
        new_p = '(' + solution(v) + ')'
        u = u[1:-1]
        u = ''.join([')' if char == '(' else '(' for char in u])
        return new_p + u