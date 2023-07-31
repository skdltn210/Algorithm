def solution(lottos, win_nums):
    cnt = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt+=1
        if lotto==0:
            zero+=1
    if cnt==0 and zero==0:
        return [6,6]
    elif cnt==0:
        return [7-zero,6]
    else:
        return [7-cnt-zero, 7-cnt]