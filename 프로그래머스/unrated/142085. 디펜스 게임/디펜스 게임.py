from heapq import heappush, heappop
def solution(n, k, enemy):
    if k<=len(enemy):
        hq = []
        for i in range(k):
            heappush(hq,(enemy[i],i))
        for j in range(k,len(enemy)):
            heappush(hq,(enemy[j],j))
            n -= heappop(hq)[0]
            if n<0:
                return j
    return len(enemy)