def solution(arr):
    zero = 0
    one = 0
    def slice(x,y,s):
        nonlocal zero
        nonlocal one
        if arr[y][x]==0:
            flag = 0
            for j in range(s):
                for i in range(s):
                    if arr[y+j][x+i]!=0:
                        flag=2
                        break
                if flag==2:
                    break
        elif arr[y][x]==1:
            flag = 1
            for j in range(s):
                for i in range(s):
                    if arr[y+j][x+i]!=1:
                        flag=2
                        break
                if flag==2:
                    break
        if flag==0:
            zero+=1
        elif flag==1:
            one+=1
        else:
            slice(x,y,s//2)
            slice(x+s//2,y,s//2)
            slice(x,y+s//2,s//2)
            slice(x+s//2,y+s//2,s//2)
    slice(0,0,len(arr))
    return [zero,one]
            
            
            