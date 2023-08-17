def solution(n):
    arr = []
    num=0
    for i in range(1,n+1):
        a = [0] * i
        num+=len(a)
        arr.append(a)
    x=0
    mode=1
    i,j=0,0
    while x<num-1:
        x+=1
        arr[i][j]=x
        if mode==1:
            i,j=i+1,j
            if i>=n or arr[i][j]!=0:
                mode=2
                i-=1
                x-=1
        elif mode==2:
            i,j=i,j+1
            if j>=len(arr[i]) or arr[i][j]!=0:
                mode=3
                j-=1
                x-=1
        elif mode==3:
            i,j=i-1,j-1
            if i<0 or arr[i][j]!=0:
                mode=1
                i,j = i+1,j+1
                x-=1
    ans = []
    for i in range(n):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                arr[i][j]=num
            ans.append(arr[i][j])
    return ans