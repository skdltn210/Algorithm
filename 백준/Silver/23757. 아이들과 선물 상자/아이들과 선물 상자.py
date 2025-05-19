import heapq

n, m = map(int, input().split())
c = list(map(int, input().split()))
w = list(map(int, input().split()))

c = [-x for x in c]
heapq.heapify(c)

possible = True
for i in w:
    if not c:
        possible = False
        break

    max_gifts = -c[0]

    if i > max_gifts:
        possible = False
        break

    heapq.heapreplace(c, -(max_gifts - i))

print(1 if possible else 0)
