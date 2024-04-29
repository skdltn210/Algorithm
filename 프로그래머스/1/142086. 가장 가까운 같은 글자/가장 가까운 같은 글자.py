def solution(s):
    arr = list(s)
    ans = []
    for i in range(len(arr)):
        cnt=1
        for j in range(i-1,-2,-1):
            if j==-1:
                ans.append(-1)
                break
            if arr[i] != arr[j]:
                cnt+=1
            else:
                ans.append(cnt)
                break
    return ans