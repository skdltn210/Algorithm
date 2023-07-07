def solution(m, musicinfos):
    arr = []
    for i in range(len(musicinfos)):
        a = musicinfos[i].split(',')
        a[3] += 'X'
        print(a)
        time = 60*(int(a[1][:2]) - int(a[0][:2])) + int(a[1][3:]) - int(a[0][3:])
        melody = []
        for j in range(len(a[3])-1):
            if a[3][j]!='#' and a[3][j+1] == '#':
                melody.append(a[3][j:j+2])
                j+=1
            elif a[3][j] == '#' and a[3][j+1] != '#':
                continue
            else:
                melody.append(a[3][j])
        song = a[2]
        melody2 = []
        for j in range(time):
            melody2.append(melody[j%len(melody)])
        arr.append([time,melody2,song,len(musicinfos)-i])
    print(arr)
    arr.sort(key = lambda x : (x[0],x[3]),reverse = True)
    sharp_cnt = 0
    for i in range(len(m)):
        if m[i] == '#':
            sharp_cnt+=1
    length = len(m) - sharp_cnt
    for i in arr:
        for j in range(len(i[1])-length+1):
            if m == ''.join(x for x in i[1][j:j+length]):
                return i[2]
    return "(None)"