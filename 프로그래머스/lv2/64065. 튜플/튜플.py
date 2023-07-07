from collections import Counter
def solution(s):
    dic = {}
    li = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    c=Counter(li)
    l = sorted(c.items(),key = lambda x:x[1],reverse=True)
    arr = [num for num,count in l]
    return arr