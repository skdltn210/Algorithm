def solution(n, k):
    fact = [1 for x in range(21)]
    fact[1]=1
    li = [x for x in range(1,n+1)]
    arr = []
    for i in range(1,21):
        fact[i] = i*fact[i-1]
    for i in range(n-1,0,-1):
        a = k//fact[i]
        b = k%fact[i]
        if b!=0:
            a+=1
        arr.append(li[a-1])
        li.remove(li[a-1])
        k=b
        if k==0:
            li.reverse()
            arr+=li
            break
    return arr