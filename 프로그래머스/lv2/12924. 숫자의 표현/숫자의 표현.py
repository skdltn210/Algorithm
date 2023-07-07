def solution(n):
    arr = [i for i in range(1,n+1)]
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == n:
                cnt+=1
                break
            elif sum > n:
                break
    return cnt