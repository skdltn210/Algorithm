import math
def solution(n, s):
    num1 = math.floor(s/n)
    num2 = s%n
    li = []
    for i in range(n):
        li.append(num1)
    for i in range(s%n):
        li[i]+=1
    if n>s:
        return [-1]
    else:
        li.sort()
        return li