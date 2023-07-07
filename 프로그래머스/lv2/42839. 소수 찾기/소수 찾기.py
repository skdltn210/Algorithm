from itertools import permutations
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    numbers = list(numbers)
    arr = []
    for i in range(1,len(numbers)+1):
        arr+=list(permutations(numbers,i))
    arr1 = []
    for i in arr:
        arr1.append(int(''.join(i)))
    arr1 = list(set(arr1))
    for i in arr1:
        if i<=1:
            continue
        if prime(i):
            cnt+=1
    return cnt
            