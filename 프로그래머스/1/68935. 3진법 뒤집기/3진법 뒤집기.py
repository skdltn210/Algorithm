def solution(n):
    three = []
    while n!=0:
        three.append(n%3)
        n//=3
    ans = 0
    cnt = 1
    for i in range(len(three)-1,-1,-1):
        ans+=three[i]*cnt
        cnt*=3
    return ans