def solution(s, n):
    str = list(s)
    ans=""
    for i in str:
        if i == " ":
            ans+=" "
            continue
        elif ord(i)>=ord('a') and ord(i)<=ord('z'):
            if ord(i)+n>ord('z'):
                i = chr(ord(i)+n-26)
                ans+=i
            else:
                i = chr(ord(i) + n)    
                ans+=i
        else:
            if ord(i)+n>ord('Z'):
                i = chr(ord(i)+n-26)
                ans+=i
            else:
                i = chr(ord(i) + n)    
                ans+=i
    return ans