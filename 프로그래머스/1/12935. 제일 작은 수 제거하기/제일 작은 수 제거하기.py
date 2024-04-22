def solution(arr):
    m=min(arr)
    ans=[]
    for i in arr:
        if(i!=m):
            ans.append(i)
    if ans!=[]:
        return ans
    else:
        return [-1]