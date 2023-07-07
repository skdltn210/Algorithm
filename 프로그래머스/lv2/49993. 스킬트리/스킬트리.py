from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    for i in range(len(skill_trees)):
        s = deque(list(skill))
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in s:
                if s[0]==skill_trees[i][j]:
                    s.popleft()
                else:
                    break
        else :
            cnt+=1
    return cnt