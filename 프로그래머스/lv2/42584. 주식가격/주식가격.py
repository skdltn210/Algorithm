def solution(prices):
    cnt = []
    for i in range(len(prices)-1):
        cnt.append(1)
    cnt.append(0)
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)-1):
            if prices[i]<=prices[j]:
                cnt[i]+=1
            else:
                break
    return cnt