from collections import Counter
def solution(X, Y):
    arr = []
    if len(X) > len(Y):
        X, Y = Y, X
    x = list(X)
    y = Counter(list(Y))
    for i in x:
        if i in y.keys():
            if y[i]==0:
                continue
            else:
                y[i]-=1
                arr.append(i)
    arr.sort(reverse=True)
    if len(arr)==0:
        return '-1'
    if arr[0]=='0':
        return '0'
    else:
        return ''.join(arr)