def solution(a, b):
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED',]
    num=0
    for i in range(a-1):
        num+=date[i]
    num+=b
    return day[num%7]