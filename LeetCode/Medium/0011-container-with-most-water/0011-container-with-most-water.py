class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        MAX=0
        while left<right:
            if height[left]<=height[right]:
                MAX=max(MAX,(right-left)*height[left])
                left+=1
            else:
                MAX=max(MAX,(right-left)*height[right])
                right-=1
        return MAX
        