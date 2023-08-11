def solution(players, callings):
    p = dict()
    for idx,player in enumerate(players):
        p[player]=idx
    for call in callings:
        pre, post = p[call]-1, p[call]
        p[players[pre]] = post
        p[players[post]] = pre
        players[pre], players[post] = players[post], players[pre]
    return players