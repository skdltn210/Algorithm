class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [tuple(grid[i]) for i in range(n)]
        cols = []
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            cols.append(col)
        cnt = 0
        for row in rows:
            for col in cols:
                if row == col:
                    cnt += 1
        return cnt