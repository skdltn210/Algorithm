def solution(n, arr1, arr2):
    def bin(num):
        a = []
        while num:
            a.append(num % 2)  
            num //= 2
        while len(a) < n:
            a.append(0) 
        a.reverse()
        return a

    a1, a2 = [], []
    for a in arr1:
        a1.append(bin(a))
    for b in arr2:
        a2.append(bin(b))
    arr = [['#' if (a1[i][j] == 1 or a2[i][j] == 1) else ' ' for j in range(n)] for i in range(n)]
    ans = []
    for i in arr:
        ans.append(''.join(i))
    return ans

