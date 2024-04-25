def solution(sizes):
    for size in sizes:
        if size[0]>size[1]:
            size[0],size[1] = size[1],size[0]
    max1,max2=0,0
    for size in sizes:
        if max1<size[0]:
            max1=size[0]
        if max2<size[1]:
            max2=size[1]
    return max1*max2