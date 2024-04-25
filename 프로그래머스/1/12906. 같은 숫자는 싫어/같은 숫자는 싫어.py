def solution(arr):
    ans = [arr[0]]
    num = arr[0]
    for i in arr:
        if i != num:
            ans.append(i)
            num=i
        else:
            continue
    return ans