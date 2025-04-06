class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        ans=0
        cnt=0
        flag=False
        while right<len(nums):
            if nums[right]==1:
                right+=1
                cnt+=1
            elif not flag and nums[right]==0:
                flag=True
                left=right
                right+=1
            elif flag and nums[right]==0:
                flag=False
                ans=max(ans,cnt)
                right=left+1
                cnt=0
        ans=max(ans,cnt)
        if not flag : ans-=1
        return ans