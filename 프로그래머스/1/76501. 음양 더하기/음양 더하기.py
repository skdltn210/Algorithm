def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i]==True:
            ans+=absolutes[i]
        elif signs[i]==False:
            ans-=absolutes[i]
    return ans