import math
def solution(fees, records):
    car = []
    time = {}
    ans = []
    for i in range(len(records)):
        s = list(map(str, records[i].split()))
        if s[2]=='IN':
            car.append((s[1],s[0],s[2]))
        elif s[2]=='OUT':
            car.append((s[1],s[0],s[2]))
    car.sort()
    for i in range(len(car)-1):
        if not car[i][0] in time:
            time[car[i][0]] = 0
        if car[i][2] == 'IN' and car[i+1][2] == 'OUT':
            in_hour, in_minute = int(car[i][1][:2]), int(car[i][1][3:])
            out_hour, out_minute = int(car[i+1][1][:2]), int(car[i+1][1][3:])
            total_minute = (out_hour-in_hour)*60 + out_minute-in_minute
            time[car[i][0]] += total_minute
        elif car[i][2]=='IN' and car[i+1][2] =='IN':
            in_hour, in_minute = int(car[i][1][:2]), int(car[i][1][3:])
            total_minute = (23-in_hour)*60 + 59-in_minute
            time[car[i][0]] += total_minute
    if car[len(car) - 1][2] == 'IN' :
        if not car[len(car) - 1][0] in time:
            time[car[len(car) - 1][0]] = 0
        in_hour, in_minute = int(car[len(car) - 1][1][:2]), int(car[len(car) - 1][1][3:])
        total_minute = (23 - in_hour) * 60 + 59 - in_minute
        time[car[len(car) - 1][0]] += total_minute
    time = list(time.values())
    for i in time:
        if i<=fees[0]:
            ans.append(fees[1])
        else:
            ans.append(fees[1]+math.ceil((i-fees[0])/fees[2])*fees[3])
    return ans