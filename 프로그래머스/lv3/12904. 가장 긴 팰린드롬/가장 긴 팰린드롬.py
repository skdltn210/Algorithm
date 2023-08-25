def solution(s):
    def expand(left, right):
        while 0<=left and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    if len(s)==1 or s==s[::-1]:
        return len(s)
    ans=0
    for i in range(len(s)-1):
        ans=max(ans, len(expand(i,i)),len(expand(i,i+1)))
    return ans