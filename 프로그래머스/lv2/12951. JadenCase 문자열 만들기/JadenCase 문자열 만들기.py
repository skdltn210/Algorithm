def solution(s):
    s2=s.split(' ')
    answer=""
    for i in range(len(s2)):
        if s2[i]:
            s2[i]=s2[i][0].upper()+s2[i][1:].lower()
        answer+= s2[i]+' '
    return answer[:-1]