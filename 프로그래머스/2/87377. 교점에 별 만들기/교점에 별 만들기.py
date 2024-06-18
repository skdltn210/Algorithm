def solution(line):
    points = set()
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            denominator = a * d - b * c
            if denominator != 0:
                x = (b * f - e * d) / denominator
                y = (e * c - a * f) / denominator
                if x.is_integer() and y.is_integer():
                    points.add((int(x), int(y)))
    
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    
    answer = []
    for y in range(max_y, min_y - 1, -1):
        row = []
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row.append('*')
            else:
                row.append('.')
        answer.append(''.join(row))
    
    return answer