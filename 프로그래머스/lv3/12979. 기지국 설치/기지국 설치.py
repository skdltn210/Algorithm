def solution(n, stations, w):
    ans = 0
    left = 1
    for i in stations:
        right = i-w-1
        if right<1:
            left = i+w+1
            continue
        ans += (right - left) // (2 * w + 1) + 1
        left = i+w+1
    if left != 1 and left<=n:
        ans += (n - left) // (2 * w + 1) + 1
    return ans

print(solution(6,[4],2))