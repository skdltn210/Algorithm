def div(num):
    cnt = 0
    n=int(num**0.5)
    for i in range(1,n+1):
        if num%i==0:
            cnt+=2
    if n*n==num:
        cnt-=1
    return cnt
    
def solution(number, limit, power):
    ans = 0
    for i in range(1,number+1):
        sword = div(i)
        if sword>limit:
            sword = power
        ans+=sword
    return ans