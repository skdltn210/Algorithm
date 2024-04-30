def solution(k, score):
    arr = []
    ans = []
    for s in score:
        arr.append(s)
        arr.sort(reverse=True)
        if len(arr) > k:
            arr.pop()
        ans.append(arr[-1])
    return ans