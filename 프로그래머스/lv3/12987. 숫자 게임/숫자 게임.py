def solution(A, B):
    ans = 0
    A.sort()
    B.sort()
    for i in A:
        for j in range(len(B)):
            if i < B[j]:
                ans+=1
                del B[j]
                break
    return ans