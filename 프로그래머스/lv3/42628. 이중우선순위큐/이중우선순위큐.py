def solution(operations):
    li = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            li.append(int(operations[i][2:]))
        elif operations[i] == 'D 1':
            if len(li)!=0:
                li.remove(max(li))
        elif operations[i] == 'D -1':
            if len(li)!=0:
                li.remove(min(li))
    if len(li)==0:
        return [0,0]
    else:
        return [max(li), min(li)]