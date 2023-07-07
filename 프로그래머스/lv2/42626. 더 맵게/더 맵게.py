from heapq import heappush, heappop, heapify
def solution(scoville, K):
    cnt = 0
    heapify(scoville)
    while True:
        if len(scoville)==1 and scoville[0] < K:
            return -1
        a = heappop(scoville)
        if a>=K:
            return cnt
        b = heappop(scoville)
        heappush(scoville,a+2*b)
        cnt+=1