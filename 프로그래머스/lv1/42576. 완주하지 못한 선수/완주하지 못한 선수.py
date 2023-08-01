from heapq import heapify,heappush,heappop
def solution(participant, completion):
    heapify(participant)
    heapify(completion)
    while completion:
        a = heappop(participant)
        b = heappop(completion)
        if a!=b:
            return a
    return participant[0]