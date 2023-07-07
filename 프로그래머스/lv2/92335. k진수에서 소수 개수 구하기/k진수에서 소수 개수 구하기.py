import math
def isprime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    cnt = 0
    arr = []
    while n>0:
        arr.append(n%k)
        n = math.floor(n/k)
    arr.reverse()
    num = ''
    for i in arr:
        num += str(i)
    n=''
    for i in range(len(num)):
        if num[i]=='0':
            if n!='' and isprime(int(n)):
                cnt+=1
            n=''
        else:
            n += str(num[i])
    if n!='' and isprime(int(n)):
        cnt+=1
    return cnt