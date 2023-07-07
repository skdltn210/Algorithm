def solution(want, number, discount):
    dic = {}
    cnt = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        dic1 = {}
        for j in range(10):
            if discount[i+j] in dic1:
                dic1[discount[i+j]] += 1
            else:
                dic1[discount[i+j]] = 1
        if dic == dic1:
            cnt+=1
    return cnt
