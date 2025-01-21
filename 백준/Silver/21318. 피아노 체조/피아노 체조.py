def solution(n, arr, music):
    desc = [0] * n
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            desc[i] = 1
    
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + desc[i - 1]
    
    for x, y in music:
        print(prefix_sum[y - 1] - prefix_sum[x - 1])

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
music = []
for _ in range(q):
    x, y = map(int, input().split())
    music.append([x, y])

solution(n, arr, music)