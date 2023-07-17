from itertools import permutations
from collections import deque

def calc(before, exp):
    after = deque()
    while before:
        a = before.popleft()
        if a != exp:
            after.append(a)
        elif a == '-' and a == exp:
                num = int(after.pop()) - int(before.popleft())
                after.append(num)
        elif a == '+' and a == exp:
                num = int(after.pop()) + int(before.popleft())
                after.append(num)
        elif a == '*' and a == exp:
                num = int(after.pop()) * int(before.popleft())
                after.append(num)
        else :
            after.append(a)
    while after:
        before.append(after.popleft())


def solution(expression):
    arr = []
    e = []
    x = 0
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '*' or expression[i] == '+':
            e.append(expression[x:i])
            e.append(expression[i])
            x = i + 1
    e.append(expression[x:])
    for i in range(len(expression)):
        if not expression[i] in arr and (expression[i] == '-' or expression[i] == '*' or expression[i] == '+'):
            arr.append(expression[i])
    p = list(permutations(arr, len(arr)))
    ans = []
    for i in p:
        a = list(i)
        de = deque(e)
        for j in a:
            calc(de,j)
        ans.append(abs(de[0]))
    return max(ans)