from math import gcd
def solution(w,h):
    cnt = gcd(w,h)
    total = w*h
    w//=cnt
    h//=cnt
    cut = w+h-1
    return total - cut*cnt
            