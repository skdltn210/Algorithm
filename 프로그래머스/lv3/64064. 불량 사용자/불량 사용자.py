from itertools import permutations
def check(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if b[i] == '*':
            continue
        elif a[i] != b[i]:
            return False
    return True

def solution(user_id, banned_id):
    a = []
    banned_id.sort(key=len)
    user = list(permutations(user_id,len(banned_id)))
    for i in user:
        arr = list(i)
        flag = 1
        for j in range(len(arr)):
            if not check(arr[j],banned_id[j]):
                flag = 0
                break
        if flag==1:
            if set(arr) not in a:
                a.append(set(arr))
    return len(a)