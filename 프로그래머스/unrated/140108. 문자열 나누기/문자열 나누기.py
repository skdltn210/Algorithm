def solution(s):
    cnt = 0
    x = s[0]
    a,b = 1,0
    for i in range(1,len(s)):
        if a==0:
            a+=1
            x=s[i]
            continue
        if x == s[i]:
            a+=1
        else:
            b+=1
        if a==b:
            cnt+=1
            a,b=0,0
    if a!=0:
        cnt+=1
    return cnt