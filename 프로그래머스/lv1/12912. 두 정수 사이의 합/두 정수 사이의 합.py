def solution(a, b):
    if a==b:
        return a
    else:
        sum = 0
        if a>=b:
            for i in range(b,a+1):
                sum+=i
        else:
            for i in range(a,b+1):
                sum+=i
        return sum