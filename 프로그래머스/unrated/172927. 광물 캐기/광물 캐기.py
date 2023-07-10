from collections import deque
def solution(picks, minerals):
    cnt = 0
    q = deque(minerals)
    arr = deque()
    m = []
    if sum(picks) < len(minerals)/5:
        q = deque(minerals[:5*sum(picks)])
    while q:
        if len(m) % 5 == 0:
            arr.append(m)
            m = []
        m.append(q.popleft())
    arr.append(m)
    arr.popleft()
    for i in range(len(arr)):
        num = 0
        for j in arr[i]:
            if j == 'diamond':
                num+=25
            elif j == 'iron':
                num+=5
            else:
                num+=1
        arr[i].append(num)
    arr = list(arr)
    arr.sort(key = lambda x : x[-1], reverse = True)
    for i in range(len(arr)):
        arr[i].pop()
    print(arr)
    for i in range(len(arr)):
        if picks[0] > 0 :
            for j in range(len(arr[i])):
                cnt+=1
            picks[0]-=1
        elif picks[0] == 0 and picks[1]>0:
            for j in range(len(arr[i])):
                if arr[i][j]=='diamond':
                    cnt+=5
                else:
                    cnt+=1
            picks[1]-=1
        elif picks[0]==0 and picks[1]==0 and picks[2]>0:
            for j in range(len(arr[i])):
                if arr[i][j]=='diamond':
                    cnt+=25
                elif arr[i][j]=='iron':
                    cnt+=5
                else:
                    cnt+=1
            picks[2]-=1
        elif picks[0]==0 and picks[1]==0 and picks[2]==0:
            break
    return cnt