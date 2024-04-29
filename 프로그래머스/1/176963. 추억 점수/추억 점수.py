def solution(name, yearning, photo):
    a = {}
    for i in range(len(name)):
        a[name[i]] = yearning[i]
    ans = []
    for i in photo:
        num = 0
        for j in i:
            if j not in a:
                continue
            else:
                num+=a[j]
        ans.append(num)
    return ans