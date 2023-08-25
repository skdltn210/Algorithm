def solution(nums):
    arr=[]
    for num in nums:
        if not num in arr:
            arr.append(num)
    print(arr)
    if len(nums)/2>=len(arr):
        return len(arr)
    else:
        return len(nums)/2