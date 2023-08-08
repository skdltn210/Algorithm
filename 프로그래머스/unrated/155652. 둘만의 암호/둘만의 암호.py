def solution(s, skip, index):
    s = list(s)
    skip = list(skip)
    alpha = []
    num = []
    arr = []
    for i in skip:
        num.append(ord(i))
    for i in range(97,123):
        if i in num:
            continue
        alpha.append(chr(i))
    l = len(alpha)
    for i in s:
        idx = alpha.index(i)
        idxx = (idx+index)%l
        arr.append(alpha[idxx])
    return ''.join(arr)