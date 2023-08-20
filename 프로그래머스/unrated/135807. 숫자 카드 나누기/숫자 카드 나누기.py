import math

def gcd(array):
    gcd=0
    for i in array:
        gcd = math.gcd(gcd,i)
    return gcd

def check(gcd,array):
    for i in array:
        if i%gcd==0:
            return 0
    return gcd

def solution(arrayA, arrayB):
    gcdA, gcdB = gcd(arrayA), gcd(arrayB)
    a, b = check(gcdA,arrayB), check(gcdB, arrayA)
    if a==0 and b==0:
        return 0
    else:
        return max(a,b)