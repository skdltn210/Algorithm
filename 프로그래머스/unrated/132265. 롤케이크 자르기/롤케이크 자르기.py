from collections import Counter
def solution(topping):
    cnt = 0
    left = set()
    right = Counter(topping)
    for i in topping:
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        left.add(i)
        if len(left) == len(right):
            cnt+=1
    return cnt        