from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=deque()
        dire=deque()
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)
    
        n = len(senate)
        
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        
        return "Radiant" if radiant else "Dire"