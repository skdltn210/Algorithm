def solution(strings, n):
    arr = []
    for i in strings:
        s = list(i)
        arr.append(s[n]+i)
    arr.sort()
    ans = []
    for i in arr:
        ans.append(i[1:])
    return ans