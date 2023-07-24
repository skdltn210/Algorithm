def solution(new_id):
    new_id = list(new_id.lower())
    arr = []
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i]=='-' or new_id[i]=='_' or new_id[i] == '.':
            arr.append(new_id[i])
            if len(arr) >= 2 and (arr[-1] == '.' and arr[-2]=='.'):
                arr.pop()
    if len(arr) > 0 and arr[0] == '.':
        del arr[0]
    if len(arr) > 0 and arr[-1] == '.':
        arr.pop()
    if len(arr) == 0:
        arr.append('a')
    if len(arr)>=16:
        while len(arr)>15:
            arr.pop()
        if arr[-1] == '.':
            arr.pop()
    while len(arr)<=2:
        c = arr[-1]
        arr.append(c)
    
    return ''.join(arr)