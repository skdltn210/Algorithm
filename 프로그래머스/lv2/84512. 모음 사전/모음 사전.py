def solution(word):
    ans = 0
    for i in range(len(word)):
        if i == 0:
            if word[i] == 'A':
                ans += 1
            elif word[i] == 'E':
                ans += 782
            elif word[i] == 'I':
                ans += 1563
            elif word[i] == 'O':
                ans += 2344
            else:
                ans += 3125
        if i == 1:
            if word[i] == 'A':
                ans += 1
            elif word[i] == 'E':
                ans += 157
            elif word[i] == 'I':
                ans += 313
            elif word[i] == 'O':
                ans += 469  
            else:
                ans += 625
        if i == 2:
            if word[i] == 'A':
                ans += 1
            elif word[i] == 'E':
                ans += 32
            elif word[i] == 'I':
                ans += 63
            elif word[i] == 'O':
                ans += 94
            else:
                ans += 125
        if i == 3:
            if word[i] == 'A':
                ans += 1
            elif word[i] == 'E':
                ans += 7
            elif word[i] == 'I':
                ans += 13
            elif word[i] == 'O':
                ans += 19
            else:
                ans += 25
        if i == 4:
            if word[i] == 'A':
                ans += 1
            elif word[i] == 'E':
                ans += 2
            elif word[i] == 'I':
                ans += 3
            elif word[i] == 'O':
                ans += 4
            else:
                ans += 5
    return ans