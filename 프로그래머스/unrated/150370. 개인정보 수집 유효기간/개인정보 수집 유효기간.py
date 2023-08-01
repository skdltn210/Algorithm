def solution(today, terms, privacies):
    today = today[:4]+today[5:7]+today[8:]
    arr = []
    for p in privacies:
        for t in terms:
            if p[-1]==t[0]:
                m = int(t[2:])
                year = int(p[:4])
                month = int(p[5:7]) + m
                day = int(p[8:10])
                    
                if day == 1:
                    day = 28
                    month -= 1
                else:
                    day -= 1
                    
                if day<10:
                    day = '0'+str(day)
                else:
                    day = str(day)
                
                year+=month//12
                month=month%12
                
                if month==0:
                    month=12
                    year-=1
                    
                if month<10:
                    month = '0'+str(month)
                else:
                    month = str(month)
                    
                arr.append(str(year)+month+day)
    ans = []
    for i in range(len(arr)):
        if today > arr[i]:
            ans.append(i+1)
    return ans
