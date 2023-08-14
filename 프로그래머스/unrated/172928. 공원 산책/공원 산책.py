def solution(park, routes):
    p = []
    for i in park:
        p.append(list(i))
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                y,x=i,j
    for route in routes:
        flag=1
        d=route[0]
        m=int(route[-1])
        if d=='E':
            if m+x<len(park[0]):
                for i in range(x+1,x+m+1):
                    if park[y][i]=='X':
                        flag=0
                        break
                if flag==1:
                    x=x+m
        if d=='W':
            if x-m>=0:
                for i in range(x-m,x):
                    if park[y][i]=='X':
                        flag=0
                        break
                if flag==1:
                    x=x-m
        if d=='N':
            if y-m>=0:
                for i in range(y-m,y):
                    if park[i][x]=='X':
                        flag=0
                        break
                if flag==1:
                    y=y-m
        if d=='S':
            if y+m<len(park):
                for i in range(y+1,y+m+1):
                    if park[i][x]=='X':
                        flag=0
                        break
                if flag==1:
                    y=y+m
    return [y,x]