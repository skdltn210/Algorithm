def solution(s):
    l=len(s)
    for i in range(1,len(s)//2+1):
        st,idx = '',0
        while idx<len(s):
            c,n = s[idx:idx+i],1
            while c == s[idx+i:idx+i+i]:
                idx,n = idx+i, n+1
            idx = idx+i
            if n==1:
                st+=c
            else:
                st+=str(n)+c
        if l>len(st):
            l=len(st)
    return l
            