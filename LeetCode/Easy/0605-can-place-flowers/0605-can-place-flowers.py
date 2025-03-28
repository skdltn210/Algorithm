from collections import deque
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        dq=deque(flowerbed)
        dq.appendleft(0)
        dq.append(0)
        for i in range(1,len(dq)-1):
            if dq[i-1]==0 and dq[i]==0 and dq[i+1]==0:
                dq[i]=1
                cnt+=1
        if cnt>=n: return True
        return False