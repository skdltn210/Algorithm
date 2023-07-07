def rotation(x1, y1, x2, y2, arr):
    m = 10000
    num = arr[x1 - 1][y1 - 1]
    if num < m:
        m = num
    for i in range(x1, x2):
        arr[i - 1][y1 - 1] = arr[i][y1 - 1]
        if arr[i - 1][y1 - 1] < m:
            m = arr[i - 1][y1 - 1]
    for i in range(y1, y2):
        arr[x2 - 1][i - 1] = arr[x2 - 1][i]
        if arr[x2 - 1][i - 1] < m:
            m = arr[x2 - 1][i - 1]
    for i in range(x2 - 1, x1 - 1, -1):
        arr[i][y2 - 1] = arr[i - 1][y2 - 1]
        if arr[i][y2 - 1] < m:
            m = arr[i][y2 - 1]
    for i in range(y2 - 1, y1, -1):
        arr[x1 - 1][i] = arr[x1 - 1][i - 1]
        if arr[x1 - 1][i] < m:
            m = arr[x1 - 1][i]
    arr[x1 - 1][y1] = num
    if arr[x1 - 1][y1] < m:
        m = arr[x1 - 1][y1]
    return m

def solution(rows, columns, queries):
    arr = [[0 for i in range(columns)] for i in range(rows)]
    x = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = x
            x += 1
    result = []
    for i in queries:
        result.append(rotation(i[0], i[1], i[2], i[3], arr))
    return result
