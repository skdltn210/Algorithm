def solution(id_list, report, k):
    count = {}
    for user in id_list:
        count[user] = [0, 0]
    rep = set()
    for r in report:
        a, b = r.split()
        if (a, b) not in rep:
            count[b][1] += 1
            rep.add((a, b))
    s = set()
    for user, c in count.items():
        if c[1] >= k:
            s.add(user)
    ans = [0] * len(id_list)
    for r in rep:  
        a, b = r
        if b in s:
            ans[id_list.index(a)] += 1
    
    return ans
