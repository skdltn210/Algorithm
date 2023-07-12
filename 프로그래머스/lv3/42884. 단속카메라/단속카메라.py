def solution(routes):
    cnt = 0
    routes.sort(key = lambda x : x[1])
    cam = -30001
    for i in range(len(routes)):
        if routes[i][0] <= cam and cam <= routes[i][1]:
            continue
        else:
            cam = routes[i][1]
            cnt+=1
    return cnt