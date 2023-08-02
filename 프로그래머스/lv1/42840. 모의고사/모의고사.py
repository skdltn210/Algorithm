def solution(answers):
    one,two,three = 0,0,0
    for i in range(len(answers)):
        if (i+1)%5 == 0:
            ans = 5
        else:
            ans = (i+1)%5
        if ans == answers[i]:
            one+=1
    for i in range(len(answers)):
        if i%2==0:
            ans = 2
        elif i%8==1:
            ans = 1
        elif i%8==3:
            ans = 3
        elif i%8==5:
            ans = 4
        elif i%8==7:
            ans = 5
        if ans == answers[i]:
            two+=1
    for i in range(len(answers)):
        if i%10<2:
            ans = 3
        elif i%10<4:
            ans = 1
        elif i%10<6:
            ans = 2
        elif i%10<8:
            ans = 4
        elif i%10<10:
            ans = 5
        if ans == answers[i]:
            three+=1
    a = max(one,two,three)
    ans = []
    if a == one:
        ans.append(1)
    if a == two:
        ans.append(2)
    if a == three:
        ans.append(3)
    return ans