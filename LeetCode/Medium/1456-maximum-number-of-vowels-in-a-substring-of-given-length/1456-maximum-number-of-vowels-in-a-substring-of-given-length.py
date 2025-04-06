class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=set(['a','e','i','o','u'])
        cnt=0
        left=0
        right=k-1
        for i in range(0,k):
            if s[i] in vowel:
                cnt+=1
        ans=cnt
        while right<len(s)-1:
            if s[left] in vowel:
                cnt-=1
            left+=1
            right+=1
            if s[right] in vowel:
                cnt+=1
            ans=max(ans,cnt)
        return ans
            
        