import math
def solution(n):
    cnt = 0
    for i in range(2,n+1):
        flag = 1
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                flag = 0
                break
        if flag==1:
            cnt+=1
        else:
            continue
    return cnt