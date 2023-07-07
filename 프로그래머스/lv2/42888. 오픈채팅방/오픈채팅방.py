def solution(record):
    uid_name = {}
    for i in range(len(record)):
        s=list(map(str,record[i].split()))
        if s[0]=="Enter" or s[0]=="Change":
            uid_name[s[1]] = s[2]
    result = []
    for i in range(len(record)):
        s=list(map(str,record[i].split()))
        if s[0]=="Enter":
            result.append(f'{uid_name[s[1]]}님이 들어왔습니다.')
        elif s[0]=="Leave":
            result.append(f'{uid_name[s[1]]}님이 나갔습니다.')  
    return result
        