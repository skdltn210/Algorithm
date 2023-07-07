def solution(k, d):
    cnt = 0
    for i in range(0,d+1,k):
        y = (d**2 - i**2)**(1/2)
        cnt += y//k + 1
    return cnt
