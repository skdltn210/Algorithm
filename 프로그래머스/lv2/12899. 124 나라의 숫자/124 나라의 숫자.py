def solution(n):
    arr = []
    while n>0 :
        x = n%3
        if x == 0 :
            x = 3
            n-=1
        arr.append(str(x))
        n = n//3
    arr.reverse()
    for i in range(len(arr)):
        if arr[i] == '3':
            arr[i]='4'
    return ''.join(arr)