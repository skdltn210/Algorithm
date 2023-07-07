import math
def solution(str1, str2):
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha() :
            s1.append(str1[i:i+2].upper())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha() :
            s2.append(str2[i:i+2].upper())
            
    intersection = []
    union = []
    
    tmp = s2.copy()
    for i in s1:
        if i in tmp:
            intersection.append(i)
            tmp.remove(i)
    
    union = s1 + s2
    tmp2 = intersection.copy()
    for i in tmp2:
        if i in union:
            union.remove(i)
    
    print(union)
    print(intersection)
    
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    
    return math.floor((len(intersection)/len(union))*65536)
