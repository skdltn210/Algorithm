def solution(n):
    cnt_1 = bin(n).count('1')
    while(1):
        n+=1
        ans = bin(n).count('1')
        if ans==cnt_1:
            return n