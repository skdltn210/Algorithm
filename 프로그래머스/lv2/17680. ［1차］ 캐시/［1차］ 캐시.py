def solution(cacheSize, cities):
    cache = []
    time = 0
    for i in range(len(cities)):
        if len(cache)<cacheSize:
            if cities[i].upper() in cache:
                cache.remove(cities[i].upper())
                cache.append(cities[i].upper())
                time+=1
            else:
                cache.append(cities[i].upper())
                time+=5
        else:
            if cities[i].upper() in cache:
                cache.remove(cities[i].upper())
                cache.append(cities[i].upper())
                time+=1
            else:
                cache.append(cities[i].upper())
                del cache[0]
                time+=5
    return time            