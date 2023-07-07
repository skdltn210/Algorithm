def solution(n):
    num = sorted(list(map(int,str(n))),reverse=True)
    ans = ""
    for i in range(len(num)):
        ans = ans + str(num[i])
    return int(ans)