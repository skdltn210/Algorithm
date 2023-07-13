def solution(begin, target, words):
    if target not in words:
        return 0
    m = 51
    visited = [0 for x in range(len(words))]
    def dfs(word, target, val):
        nonlocal m
        if word == target:
            if m > val:
                m = val
        else:
            for i in range(len(words)):
                cnt = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt+=1
                if cnt == 1 and visited[i] == 0:
                    visited[i] = 1
                    dfs(words[i],target,val+1)
                    visited[i] = 0
    dfs(begin, target, 0)
    return m