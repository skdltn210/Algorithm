import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solution(nums):
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                num = nums[i]+nums[j]+nums[k]
                if is_prime(num): cnt+=1
    return cnt