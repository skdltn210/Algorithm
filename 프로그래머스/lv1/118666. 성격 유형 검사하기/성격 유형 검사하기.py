def solution(survey, choices):
    point = [[0,0],[0,0],[0,0],[0,0]]
    s = ''
    for i in range(len(survey)):
        if survey[i][0] == 'A':
            if choices[i]==1: point[3][0]+=3
            if choices[i]==2: point[3][0]+=2
            if choices[i]==3: point[3][0]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[3][1]+=1
            if choices[i]==6: point[3][1]+=2
            if choices[i]==7: point[3][1]+=3
        if survey[i][0] == 'N':
            if choices[i]==1: point[3][1]+=3
            if choices[i]==2: point[3][1]+=2
            if choices[i]==3: point[3][1]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[3][0]+=1
            if choices[i]==6: point[3][0]+=2
            if choices[i]==7: point[3][0]+=3
        if survey[i][0] == 'C':
            if choices[i]==1: point[1][0]+=3
            if choices[i]==2: point[1][0]+=2
            if choices[i]==3: point[1][0]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[1][1]+=1
            if choices[i]==6: point[1][1]+=2
            if choices[i]==7: point[1][1]+=3
        if survey[i][0] == 'F':
            if choices[i]==1: point[1][1]+=3
            if choices[i]==2: point[1][1]+=2
            if choices[i]==3: point[1][1]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[1][0]+=1
            if choices[i]==6: point[1][0]+=2
            if choices[i]==7: point[1][0]+=3
            
        if survey[i][0] == 'J':
            if choices[i]==1: point[2][0]+=3
            if choices[i]==2: point[2][0]+=2
            if choices[i]==3: point[2][0]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[2][1]+=1
            if choices[i]==6: point[2][1]+=2
            if choices[i]==7: point[2][1]+=3
        if survey[i][0] == 'M':
            if choices[i]==1: point[2][1]+=3
            if choices[i]==2: point[2][1]+=2
            if choices[i]==3: point[2][1]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[2][0]+=1
            if choices[i]==6: point[2][0]+=2
            if choices[i]==7: point[2][0]+=3
        if survey[i][0] == 'R':
            if choices[i]==1: point[0][0]+=3
            if choices[i]==2: point[0][0]+=2
            if choices[i]==3: point[0][0]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[0][1]+=1
            if choices[i]==6: point[0][1]+=2
            if choices[i]==7: point[0][1]+=3
        if survey[i][0] == 'T':
            if choices[i]==1: point[0][1]+=3
            if choices[i]==2: point[0][1]+=2
            if choices[i]==3: point[0][1]+=1
            if choices[i]==4: continue
            if choices[i]==5: point[0][0]+=1
            if choices[i]==6: point[0][0]+=2
            if choices[i]==7: point[0][0]+=3
    if point[0][0]>=point[0][1]:
        s+='R'
    else:
        s+='T'
    if point[1][0]>=point[1][1]:
        s+='C'
    else:
        s+='F'
    if point[2][0]>=point[2][1]:
        s+='J'
    else:
        s+='M'
    if point[3][0]>=point[3][1]:
        s+='A'
    else:
        s+='N'
    return s