import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        n = len(costs)
        left_ptr = 0
        right_ptr = n - 1
        left = []
        right = []
        
        for i in range(min(candidates, n)):
            heapq.heappush(left, (costs[i], i))
            left_ptr = i + 1
            
        for i in range(max(left_ptr, n - candidates), n):
            heapq.heappush(right, (costs[i], i))
            right_ptr = i - 1
            
        for i in range(k):
            if not left or (right and left[0][0] > right[0][0]):
                cost, idx = heapq.heappop(right)
                ans += cost
                if left_ptr <= right_ptr:
                    heapq.heappush(right, (costs[right_ptr], right_ptr))
                    right_ptr -= 1
            else:
                cost, idx = heapq.heappop(left)
                ans += cost
                if left_ptr <= right_ptr:
                    heapq.heappush(left, (costs[left_ptr], left_ptr))
                    left_ptr += 1
        
        return ans