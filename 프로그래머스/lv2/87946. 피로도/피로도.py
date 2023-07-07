import itertools
def solution(k, dungeons):
    MAX = 0
    arr = list(itertools.permutations(dungeons,len(dungeons)))
    for i in range(len(arr)):
        cnt = 0
        num = k
        for j in range(len(dungeons)):
            if num>=arr[i][j][0]:
                cnt+=1
                num-=arr[i][j][1]
            if cnt>MAX:
                MAX = cnt
        num = k
    return MAX