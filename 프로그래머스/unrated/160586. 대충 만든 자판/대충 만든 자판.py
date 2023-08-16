def solution(keymap, targets):
    arr = []
    k = []
    maxlen = 0
    for i in keymap:
        if len(i)>maxlen:
            maxlen = len(i)
    for i in keymap:
        s = ''
        if len(i)<maxlen:
            for j in range(maxlen-len(i)):
                s+='#'
        k.append(i+s)
        
    for target in targets:
        cnt=0
        for i in range(len(target)):
            cntt=0
            flag=0
            for a in range(maxlen):
                cntt+=1
                for b in range(len(keymap)):
                    if target[i] == k[b][a]:
                        flag=1
                        break
                if flag==1:
                    break
            if flag==0:
                arr.append(-1)
                break
            cnt+=cntt
        if flag==1:
            arr.append(cnt)
    return arr