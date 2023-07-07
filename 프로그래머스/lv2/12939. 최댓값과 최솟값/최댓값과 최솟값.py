def solution(s):
    min = 9999999999
    max = -9999999999
    numbers = list(map(int,str(s).split()))
    for i in range(len(numbers)):
        if min>numbers[i] :
            min=numbers[i]
        if max<numbers[i]:
            max = numbers[i]
    
    return f"{min} {max}"