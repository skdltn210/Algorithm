def solution(s):
    ans = ''
    idx = 0
    for spell in s:
        if spell == ' ':
            ans += ' '
            idx = 0
        else:
            if idx % 2 == 0:
                ans += spell.upper()
            else:
                ans += spell.lower()
            idx += 1
    return ans