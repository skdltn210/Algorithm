def solution(k, ranges):
    arr = []
    arr2 = []
    result = []
    n = k
    i=0
    
    while n>1:
        arr.append([i,n])
        if n%2==0:
            n//=2
        else:
            n=n*3+1
        i+=1
    arr.append([i,n])
    
    l = len(arr)
    
    for r in ranges:
        if r[0]==0 and r[1]==0:
            s=0
            for a in range(len(arr)-1):
                s+=(arr[a][1]+arr[a+1][1])/2
            result.append(s)
            
        elif r[0]>l+r[1]-1:
            result.append(-1)
            
        else:
            s=0
            for a in range(r[0],l+r[1]-1):
                s+=(arr[a][1]+arr[a+1][1])/2
            result.append(s)
        
        
    return result