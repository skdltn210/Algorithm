from collections import Counter
def solution(gems):
    l = len(set(gems))
    arr = []
    left = 0
    c = Counter()
    for right in range(len(gems)):
        c[gems[right]]+=1
        right+=1
        while len(c) == l:
            c[gems[left]]-=1
            if c[gems[left]]==0:
                del c[gems[left]]
            left+=1
            arr.append([left,right])
    
    arr.sort(key = lambda x: (x[1]-x[0],x[0]))
    return arr[0]