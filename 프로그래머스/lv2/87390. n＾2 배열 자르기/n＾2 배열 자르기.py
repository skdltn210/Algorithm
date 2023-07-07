import math
def solution(n, left, right):
    arr = []
    for i in range(left,right+1):
        a, b = math.floor(i/n), i%n
        arr.append(max(a,b)+1)
    return arr