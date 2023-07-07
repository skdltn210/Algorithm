import math
def solution(dirs):
    x,y = 5,5
    visited = [[0]*11 for i in range(11)]
    visited[x][y]=1
    route = set()
    for i in range(len(dirs)):
        a,b = x,y
        if dirs[i] == 'U':
            y+=1
            if y==11:
                y-=1
        elif dirs[i] == 'D':
            y-=1
            if y==-1:
                y+=1
        elif dirs[i] == 'L':
            x-=1
            if x==-1:
                x+=1
        elif dirs[i] == 'R':
            x+=1
            if x==11:
                x-=1
        c,d = x,y
        if a==c and b==d:
            continue
        route.add((((a,b),(c,d)),((c,d),(a,b))))
        route.add((((c, d), (a, b)), ((a, b), (c, d))))
    return math.floor(len(route)/2)