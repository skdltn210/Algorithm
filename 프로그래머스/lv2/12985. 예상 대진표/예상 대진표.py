import math
def solution(n,a,b):
    cnt=1
    if b<a:
        a,b = b,a
    while True:
        if a+1==b and a%2==1:
            return cnt
        else:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            cnt+=1
