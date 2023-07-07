def solution(s):
    a=b=0
    for i in range(len(s)):
        if b>a:
            return False
        elif s[i]=='(':
            a+=1
        else:
            b+=1
    return a==b