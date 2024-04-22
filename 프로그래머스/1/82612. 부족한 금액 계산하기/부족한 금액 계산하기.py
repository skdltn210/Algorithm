def solution(price, money, count):
    tot = 0
    for i in range(count):
        tot += price*(i+1)
    if(tot<=money):
        return 0
    return tot-money