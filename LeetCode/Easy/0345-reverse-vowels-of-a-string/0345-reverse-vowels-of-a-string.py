class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=list(s)
        vowels=set('aeiouAEIOU')
        v=[]
        for i in range(len(s)):
            if arr[i] in vowels: v.append(s[i])
        v.reverse()
        idx=0
        for i in range(len(arr)):
            if arr[i] in vowels: 
                arr[i]=v[idx]
                idx+=1
        return ''.join(arr)
        