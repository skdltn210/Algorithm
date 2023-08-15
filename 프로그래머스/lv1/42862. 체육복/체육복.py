def solution(n, lost, reserve):
    arr = [1 for x in range(n)]
    for i in lost:
        arr[i-1] -=1
    for r in reserve:
        arr[r-1] +=1
    for i in range(n):
        if arr[i]==2:
            if i-1>=0 and arr[i-1]==0:
                arr[i-1]=1
                arr[i]=1
            elif i+1<n and arr[i+1]==0:
                arr[i+1]=1
                arr[i]=1
            
    cnt=0
    for i in arr:
        if i>=1:
            cnt+=1
    return cnt