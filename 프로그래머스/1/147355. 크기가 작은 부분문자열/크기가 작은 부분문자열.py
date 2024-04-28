def solution(t, p):
    l = len(p)
    s = list(t)
    cnt=0
    for i in range(len(t)-l+1):
        num = ""
        for j in range(i,i+l):
            num+=s[j]
        if num<=p:
            cnt+=1
    return cnt