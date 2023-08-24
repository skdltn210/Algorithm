def solution(name):
    if set(name) == {'A'}:
        return 0
    answer = 10000
    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] 
        r_l = name[i: :-1] + name[i+1:][::-1] 
        for n in [l_r,r_l]:
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c)-ord('A'), (ord('Z')+1) - ord(c)) for c in n ]
            answer = min(answer, i + (len(cnt)-1) + sum(cnt))
    return answer