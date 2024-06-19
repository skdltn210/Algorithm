import math
def solution(r1, r2):
    ans=0
    for x in range(1,r2+1):
        a=math.sqrt(r2*r2-x*x)
        a=int(a)*2+1
        b=0
        if x<r1:
            b=math.sqrt(r1*r1-x*x)
            if b==int(b):               
                b=b*2-1                  
            else:
                b=int(b)                
                b=b*2+1
        ans+=a-b
    ans=2*ans
    ans=ans+2*(r2-r1+1)
    return ans    