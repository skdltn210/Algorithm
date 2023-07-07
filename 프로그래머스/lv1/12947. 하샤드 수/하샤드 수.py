def solution(x):
    n = sum(map(int,str(x)))
    if x%n==0:
        return True
    else:
        return False