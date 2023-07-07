def solution(n):
    ans = -1
    for i in range(1,n+1):
        if n/i == i and n%i ==0 :
            ans = (i+1)**2
            break
    return ans