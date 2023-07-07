import math
def solution(n, t, m, p):
    ans = ''
    num = []
    i=1
    num.append('0')
    while len(num)<t*m:
        number = i
        s = ''
        while number > 0:
            if number%n < 10:
                s += str(number%n)
            elif number%n == 10:
                s+='A'
            elif number%n == 11:
                s+='B'
            elif number%n == 12:
                s+='C'
            elif number%n == 13:
                s+='D'
            elif number%n == 14:
                s+='E'
            elif number%n == 15:
                s+='F'
            number = math.floor(number/n)
        s = list(s)
        s.reverse()
        for j in range(len(s)):
            num.append(s[j])
            while len(num)>t*m:
                num.pop()
        i+=1
    k = m%p
    if k == 0:
        k=m-1
    else:
        k-=1
    for j in range(p-1,len(num),m):
        ans+=num[j]
    return ans