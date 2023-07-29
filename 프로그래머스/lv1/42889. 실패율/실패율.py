def solution(N, stages):
    arr = []
    tot = len(stages)
    for i in range(1,N+1):
        if tot==0:
            arr.append([i,0])
        else:
            cnt = 0
            for stage in stages:
                if stage == i:
                    cnt+=1
            arr.append([i,cnt/tot])
            tot -= cnt
    arr.sort(key = lambda x : x[1],reverse = True)
    ans = [i[0] for i in arr]
    return ans