def solution(food):
    arr = []
    for f in food:
        if f%2==0:
            arr.append(f)
        elif f==1:
            arr.append(0)
        else:
            arr.append(f-1)
    print(arr)
    ans = ""
    for i in range(len(arr)):
        cnt = arr[i]/2
        if arr[i] != 0:
            while cnt>0:
                ans+=str(i)
                cnt-=1
    ans+=str(0)
    for i in range(len(arr)-1,-1,-1):
        cnt = arr[i]/2
        if arr[i] != 0:
            while cnt>0:
                ans+=str(i)
                cnt-=1
    return ans
