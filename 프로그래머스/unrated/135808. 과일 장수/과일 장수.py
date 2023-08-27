def solution(k, m, score):
    score.sort(reverse=True)
    box=len(score)//m
    arr=[]
    idx=0
    for i in range(box):
        a=[]
        for j in range(m):
            a.append(score[idx+j])
        idx+=m
        arr.append(a)
    ans=0
    for i in arr:
        ans+=min(i)*m
    return ans
