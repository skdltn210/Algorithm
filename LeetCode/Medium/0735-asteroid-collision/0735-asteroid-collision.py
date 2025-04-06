from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq=deque(asteroids)
        arr=[dq.popleft()]
        while len(dq)>0:
            x=dq.popleft()
            flag=True
            while len(arr)>0 and (arr[-1]>=0 and x<0):
                if abs(arr[-1])>abs(x): 
                    flag=False
                    break
                elif abs(arr[-1]<abs(x)): arr.pop()
                else: 
                    arr.pop()
                    flag=False
                    break
            if(flag): arr.append(x)
        return arr