def solution(c):
    c.sort(reverse=True)
    for i in range(len(c)):
        if c[i]<=i:
            return i
    return len(c)