def solution(brown, yellow):
    for a in range(1,int(brown/2)):
        if yellow%a==0:
            b=yellow/a
        else:
            continue
        if (2*(a+2)+2*b)==brown:
            return[b+2,a+2]