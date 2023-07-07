def solution(x, n):
    num = x
    answer = []
    for i in range (n):
        answer.append(x)
        x+=num
    return answer