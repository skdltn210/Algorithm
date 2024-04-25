def solution(users, emoticons):
    users.sort(reverse=True)
    emoticons.sort()
    discount = [40, 30, 20, 10]
    dis_arr = [[d1, d2, d3, d4,d5,d6,d7] for d1 in discount for d2 in discount for d3 in discount for d4 in discount for d5 in discount for d6 in discount for d7 in discount ]
    arr = []
    for dis in dis_arr:
        dis_emoticon = [[d,e - e * d / 100] for e, d in zip(emoticons, dis)]
        cnt,tot = 0,0
        for user in users:
            amount = 0
            for j in dis_emoticon:
                if j[0]>=user[0]:
                    amount+=j[1]
            if amount>=user[1]:
                cnt+=1
            else:
                tot+=amount
        arr.append([cnt,tot])
    arr.sort(reverse=True)
    return arr[0]
            