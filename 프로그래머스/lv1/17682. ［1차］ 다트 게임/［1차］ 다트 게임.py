def solution(dartResult):
    point = []
    i = 0
    while i < len(dartResult):
        if dartResult[i] == 'S':
            point[-1] = int(point[-1])
        elif dartResult[i] == 'D':
            point[-1] = int(point[-1]) ** 2
        elif dartResult[i] == 'T':
            point[-1] = int(point[-1]) ** 3
        elif dartResult[i].isdigit():
            if dartResult[i] == '1' and i + 1 < len(dartResult) and dartResult[i + 1] == '0':
                point.append(10)
                i += 1
            else:
                point.append(int(dartResult[i]))
        elif dartResult[i] == '*':
            if len(point) >= 2:
                point[-1] *= 2
                point[-2] *= 2
            else:
                point[-1] *= 2
        elif dartResult[i] == '#':
            point[-1] *= -1
        i += 1
    return sum(point)
