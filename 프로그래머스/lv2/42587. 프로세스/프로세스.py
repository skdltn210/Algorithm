def solution(priorities, location):
    process = []
    cnt = 1
    for i in range(len(priorities)):
        process.append((i,priorities[i]))
    while len(process)>0:
        max = 0
        for i in range(len(process)):
            if max < process[i][1]:
                max = process[i][1]
        if process[0][1] == max : 
            if process[0][0] == location:
                return cnt
            else:
                del process[0]
                cnt+=1
        else:
            process.append((process[0][0],process[0][1]))
            del process[0] 