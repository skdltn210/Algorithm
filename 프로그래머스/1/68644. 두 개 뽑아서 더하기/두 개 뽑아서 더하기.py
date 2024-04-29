def solution(numbers):
    arr = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            s = numbers[i]+numbers[j]
            if s not in arr:
                arr.append(s)
    arr.sort()
    return arr