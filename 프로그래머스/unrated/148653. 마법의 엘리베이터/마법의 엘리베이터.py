def solution(storey):
    cnt = 0
    while storey:
        num = storey%10
        storey = storey//10
        if num > 5 or (num == 5 and storey%10 >= 5):
            cnt += 10 - num
            storey+=1
        else:
            cnt+=num
    return cnt