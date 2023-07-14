def solution(genres, plays):
    music = []
    g = {}
    for i in range(len(plays)):
        music.append([genres[i],plays[i],i])
        if not genres[i] in g:
            g[genres[i]] = plays[i]
        else:
            g[genres[i]] += plays[i]
    li = []
    for a,b in g.items():
        li.append([a,b])
    li.sort(key = lambda x : (x[1],x[0]), reverse = True)
    music.sort(key = lambda x: (x[1]), reverse = True)
    arr = []
    for i in range(len(li)):
        cnt = 0
        for j in range(len(music)):
            if li[i][0] == music[j][0]:
                arr.append(music[j][2])
                cnt+=1
            if cnt==2:
                break
    return arr