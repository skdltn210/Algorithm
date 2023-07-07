from heapq import heapify, heappush, heappop
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [(-1)*work for work in works]
    heapify(works)
    for i in range(n):
        tmp = heappop(works)
        tmp+=1
        heappush(works,tmp)
    return sum([work ** 2 for work in works])