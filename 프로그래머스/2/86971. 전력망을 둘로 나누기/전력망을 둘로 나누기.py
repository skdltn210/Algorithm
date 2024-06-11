def solution(n, wires):
    ans=100
    arr = []
    wires.sort()
    for i in range(len(wires)):
        w = wires[:i] + wires[i+1:]
        arr.append(w[0][0])
        arr.append(w[0][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
        for j in range(1,len(w)):
            if w[j][0] not in arr and w[j][1] in arr:
                arr.append(w[j][0])
            if w[j][1] not in arr and w[j][0] in arr:
                arr.append(w[j][1])
                
                
        if abs(len(arr)-(n-len(arr)))<ans:
            ans = abs(len(arr)-(n-len(arr)))
        arr = []
    return ans