import math

def solution(n, words):
    word = set()
    for i in range(len(words)):
        a = (i % n) + 1
        b = math.ceil((i + 1) / n)
        if i > 0 and (words[i - 1][-1] != words[i][0] or words[i] in word):
            return [a, b]
        word.add(words[i])
    return [0, 0]