def solution(bandage, health, attacks):
    max_health = health
    t = attacks[-1][0]
    success = 0
    attack_time = []
    for i in attacks:
        attack_time.append(i[0])
    for i in range(t+1):
        if i not in attack_time:
            health+=bandage[1]
            if health>=max_health:
                health=max_health
            success+=1
            if success==bandage[0]:
                health+=bandage[2]
                if health>=max_health:
                    health=max_health
                success=0
        else:
            success=0
            for j in attacks:
                if j[0]==i:
                    health-=j[1]
                if health<0:
                    return -1
    if health>0:
        return health
    else:
        return -1