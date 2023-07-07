def solution(numbers, target):
    cnt = 0
    def dfs(idx, sum):
        nonlocal cnt
        if idx == len(numbers):
            if sum == target:
                cnt += 1
            return
        dfs(idx+1, sum + numbers[idx])
        dfs(idx+1, sum - numbers[idx])
    dfs(0,0)
    return cnt