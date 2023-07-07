def solution(sequence, k):
    left, right = len(sequence)-1, len(sequence)-1
    s = sequence[-1]
    arr = []
    while left > -1:
        if s == k:
            arr.append([left, right,right-left])
            left -= 1
            s+=sequence[left]
        elif s < k:
            left-=1
            s+=sequence[left]
        else:
            s-=sequence[right]
            right-=1
    arr.sort(key = lambda x : (x[2],x[0]))
    return [arr[0][0], arr[0][1]]