def solution(elements):
    sums = []
    sums.extend(elements)
    for i in range(len(elements)+1): 
        if i == 0 or i == 1:
            continue
        for j in range(len(elements)):
            sums.append(sums[(i-2)*len(elements)+j] + sums[(j+i-1)%len(elements)   ]) 
    return len(list(set(sums)))