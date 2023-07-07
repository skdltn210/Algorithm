def solution(files):
    arr = []
    for index, file in enumerate(files):
        file = file.lower()
        arr.append([index,'',''])
        num = False
        for f in file:
            if f.isdigit():
                num = True
                arr[-1][2] += f
            else:
                if num:
                    break
                arr[-1][1] += f
        arr[-1][2] = int(arr[-1][2])
    print(arr)
    arr = sorted(arr, key = lambda x : (x[1],x[2],x[0]))
    return [files[x[0]] for x in arr]