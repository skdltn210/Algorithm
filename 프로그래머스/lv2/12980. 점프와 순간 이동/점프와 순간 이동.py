def solution(n):
    cnt=0
    while True :
        if n==1:
            return cnt+1
        if n%2==1:
            n-=1
            cnt+=1
        else :
            n/=2