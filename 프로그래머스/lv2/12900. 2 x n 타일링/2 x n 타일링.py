def solution(n):
    a,b = 1,2
    for i in range(3,n+1):
        b,a = a+b,b
    return b%1000000007