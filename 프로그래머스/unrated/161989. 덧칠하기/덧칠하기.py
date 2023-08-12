def solution(n, m, section):
    cnt=0
    p=0
    for s in section:
        if p<s:
            p=s+m-1
            cnt+=1
    return cnt