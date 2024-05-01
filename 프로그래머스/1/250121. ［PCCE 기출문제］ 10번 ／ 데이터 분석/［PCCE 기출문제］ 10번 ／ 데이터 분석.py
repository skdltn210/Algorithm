def solution(data, ext, val_ext, sort_by):
    ans = []
    if ext == 'code':
        for d in data:
            if d[0]<val_ext:
                ans.append(d)
        if sort_by == 'code':
            ans.sort(key = lambda x : x[0])
        elif sort_by == 'date':
            ans.sort(key = lambda x : x[1])
        elif sort_by == 'maximum':
            ans.sort(key = lambda x : x[2])
        elif sort_by == 'remain':
            ans.sort(key = lambda x : x[3])
    elif ext == 'date':
        for d in data:
            if d[1]<val_ext:
                ans.append(d)
        if sort_by == 'code':
            ans.sort(key = lambda x : x[0])
        elif sort_by == 'date':
            ans.sort(key = lambda x : x[1])
        elif sort_by == 'maximum':
            ans.sort(key = lambda x : x[2])
        elif sort_by == 'remain':
            ans.sort(key = lambda x : x[3])
    elif ext == 'maximum':
        for d in data:
            if d[2]<val_ext:
                ans.append(d)
        if sort_by == 'code':
            ans.sort(key = lambda x : x[0])
        elif sort_by == 'date':
            ans.sort(key = lambda x : x[1])
        elif sort_by == 'maximum':
            ans.sort(key = lambda x : x[2])
        elif sort_by == 'remain':
            ans.sort(key = lambda x : x[3])
    elif ext == 'remain':
        for d in data:
            if d[3]<val_ext:
                ans.append(d)
        if sort_by == 'code':
            ans.sort(key = lambda x : x[0])
        elif sort_by == 'date':
            ans.sort(key = lambda x : x[1])
        elif sort_by == 'maximum':
            ans.sort(key = lambda x : x[2])
        elif sort_by == 'remain':
            ans.sort(key = lambda x : x[3])
    return ans