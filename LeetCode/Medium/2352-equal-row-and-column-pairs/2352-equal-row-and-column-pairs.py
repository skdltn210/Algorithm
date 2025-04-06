class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        Set=set()
        cnt=0
        for g in grid:
            g=tuple(g)
            if g in Set: cnt+=1
            Set.add(g)
        for i in range(len(grid[0])):
            arr=[]
            for j in range(len(grid)):
                arr.append(grid[j][i])
            if tuple(arr) in Set: cnt+=1
        return cnt