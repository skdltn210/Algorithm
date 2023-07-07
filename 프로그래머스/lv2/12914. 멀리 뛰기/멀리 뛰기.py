def solution(n):
    curr, next = 0,1
    for i in range (n):
        curr, next = next, curr+next
    return next%1234567