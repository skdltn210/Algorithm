def solution(s):
    cnt_0 = 0
    cnt = 0
    num = list(map(int,str(s)))
    num2 = []
    while not(num[0]==1 and len(num)==1):
        for i in range(len(num)):
            if num[i]==1:
                num2.append(1)
            else:
                cnt_0 +=1
        num = list(map(int,bin(len(num2))[2:]))
        num2 = []
        cnt+=1
        
    return [cnt,cnt_0]