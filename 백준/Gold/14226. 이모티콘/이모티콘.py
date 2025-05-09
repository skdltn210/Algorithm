from collections import deque

s = int(input())


def bfs(s):
    q = deque([(1, 0, 0)])
    visited = set([(1, 0)])
    while q:
        screen, clipboard, time = q.popleft()
        if screen == s:
            return time
        next_state = (screen, screen)
        if next_state not in visited:
            q.append((screen, screen, time + 1))
            visited.add(next_state)
        if clipboard > 0:
            next_state = (screen + clipboard, clipboard)
            if next_state not in visited:
                q.append((screen + clipboard, clipboard, time + 1))
                visited.add(next_state)
        if screen > 0:
            next_state = (screen - 1, clipboard)
            if next_state not in visited:
                q.append((screen - 1, clipboard, time + 1))
                visited.add(next_state)


print(bfs(s))