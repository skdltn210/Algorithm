def solution(numbers, hand):
    left_a, left_b, right_a, right_b = 3,0,3,2
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    ans = []
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            ans.append('L')
            for i in range(4):
                for j in range(3):
                    if arr[i][j]==number:
                        left_a,left_b = i,j
                        break
                        
        if number == 3 or number == 6 or number == 9:
            ans.append('R')
            for i in range(4):
                for j in range(3):
                    if arr[i][j]==number:
                        right_a,right_b = i,j
                        break
                        
        if number == 2 or number == 5 or number == 8 or number == 0:
            for i in range(4):
                for j in range(3):
                    if arr[i][j]==number:
                        a,b = i,j
                        
            if (max(left_a,a)-min(left_a,a))+(max(left_b,b)-min(left_b,b)) > (max(right_a,a)-min(right_a,a))+(max(right_b,b)-min(right_b,b)):
                ans.append('R')
                right_a, right_b = a,b
                
            elif (max(left_a,a)-min(left_a,a))+(max(left_b,b)-min(left_b,b)) < (max(right_a,a)-min(right_a,a))+(max(right_b,b)-min(right_b,b)):
                ans.append('L')
                left_a, left_b = a,b
                
            else:
                if hand == 'right':
                    ans.append('R')
                    right_a, right_b = a,b
                else:
                    ans.append('L')
                    left_a, left_b = a,b
    return ''.join(ans)