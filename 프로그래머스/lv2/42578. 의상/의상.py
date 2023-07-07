def solution(clothes):
    clo = {}
    for i in range(len(clothes)):
        clo[clothes[i][1]]=0
    for i in range(len(clothes)):
        clo[clothes[i][1]]+=1
    c = list(clo.values())
    ans = 1
    for i in range(len(c)):
        c[i]+=1
        ans *= c[i]
    return ans-1
    