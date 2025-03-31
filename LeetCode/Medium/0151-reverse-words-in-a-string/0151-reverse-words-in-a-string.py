class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        str=[]
        for i in s:
            if i!="":str.append(i)
        left,right=0,len(str)-1
        while left<right:
            str[left],str[right]=str[right],str[left]
            left+=1
            right-=1
        return " ".join(str)