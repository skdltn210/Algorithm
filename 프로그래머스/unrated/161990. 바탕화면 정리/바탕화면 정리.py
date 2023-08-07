def solution(wallpaper):
    w = []
    for i in wallpaper:
        i=list(i)
        w.append(i)
    arr = []
    for i in range(len(w)):
        for j in range(len(w[0])):
            if w[i][j]=='#':
                arr.append([i,j])
    lux,luy,rdx,rdy = len(w[0])+1,len(w)+1,0,0
    for a in arr:
        if a[1]<lux:
            lux=a[1]
        if a[1]>rdx:
            rdx=a[1]
    for a in arr:
        if a[0]<luy:
            luy=a[0]
        if a[0]>rdy:
            rdy=a[0]
    rdx+=1
    rdy+=1
    return [luy,lux,rdy,rdx]