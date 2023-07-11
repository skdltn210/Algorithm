import sys
sys.setrecursionlimit(50000000)
def solution(maps):
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    arr = []
    print(maps)
    visited = [[0 for x in range(len(maps[0]))] for y in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                visited[i][j] = 1
    print(visited)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    s = 0
    def dfs(x, y):
        nonlocal s
        if visited[y][x] == 0:
            s += int(maps[y][x])
            visited[y][x] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and visited[ny][nx] == 0:
                    dfs(nx, ny)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            dfs(j, i)
            if s != 0:
                arr.append(s)
            s = 0

    if not arr:
        arr.append(-1)
    arr.sort()
    return arr
