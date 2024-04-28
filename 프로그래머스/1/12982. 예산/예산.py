def solution(d, budget):
    d.sort()
    ans = 0
    for i in d:
        if i<=budget:
            budget-=i
            ans+=1
        else:
            break
    return ans
        