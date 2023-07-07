def solution(numbers):
    result = []
    for i in numbers:
        if i%2 == 0:
            result.append(i+1)
        else:
            num = list(bin(i)[2:])
            if not '0' in num:
                num.insert(0,'0')
            li = []
            for j in range(len(num)-1,-1,-1):
                if num[j]=='1':
                    li.append('0')
                else:
                    li.insert(0,'1')
                    break
            n = ''.join(li)
            d = int(n,2)
            result.append(int(i+d-d/2))
    return result