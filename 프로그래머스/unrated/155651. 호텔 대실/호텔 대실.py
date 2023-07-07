def solution(book_time):
    arr = []
    for i in book_time:
        arr.append([60*int(i[0][:2])+int(i[0][3:]),60*int(i[1][:2])+int(i[1][3:])+10])
    room = 0
    for i in range(1440):
        cnt = 0
        for book in arr:
            start, end = book
            if start <= i < end:
                cnt += 1
                if cnt > room:
                    room = cnt
    return room