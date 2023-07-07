def solution(places):
    ans = []
    for i in range(5):
        for j in range(5):
            places[i][j] = list(places[i][j])
        flag = 0
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    if k+1 < 5 and places[i][j][k + 1] == 'P' :
                        ans.append(0)
                        flag = 1
                        break
                    if k+2<5 and places[i][j][k+2] == 'P' and places[i][j][k+1] == 'O':
                        ans.append(0)
                        flag = 1
                        break
                    if j+1<5 and places[i][j+1][k] == 'P':
                        ans.append(0)
                        flag = 1
                        break
                    if j+2<5 and places[i][j+2][k] == 'P' and places[i][j+1][k] == 'O':
                        ans.append(0)
                        flag = 1
                        break
                    if k+1<5 and j+1 < 5 and places[i][j+1][k+1] == 'P' and  (places[i][j][k+1] == 'O' or places[i][j+1][k] == 'O'):
                        ans.append(0)
                        flag = 1
                        break
                    if k-1>=0 and j-1 >=0 and places[i][j-1][k-1] == 'P' and  (places[i][j][k-1] == 'O' or places[i][j-1][k] == 'O'):
                        ans.append(0)
                        flag = 1
                        break
                    if k+1<5 and j-1 >=0 and places[i][j-1][k+1] == 'P' and  (places[i][j][k+1] == 'O' or places[i][j-1][k] == 'O'):
                        ans.append(0)
                        flag = 1
                        break
                    if k-1>=0 and j+1 < 5 and places[i][j+1][k-1] == 'P' and  (places[i][j][k-1] == 'O' or places[i][j+1][k] == 'O'):
                        ans.append(0)
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 0:
            ans.append(1)
        print(ans)
    return ans