def solution(n):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    arr = [[0 for i in range(n)]for i in range(n)]
    i=1
    y,x = 0,0
    idx=0
    while i<=n*n:
        arr[y][x]=i
        if x+dx[idx]<0 or y+dy[idx]<0 or x+dx[idx]>n-1 or y+dy[idx]>n-1 or arr[y+dy[idx]][x+dx[idx]] != 0:
            idx+=1
            if idx>3:
                idx=0
        x+=dx[idx]
        y+=dy[idx]
        i+=1
    return arr