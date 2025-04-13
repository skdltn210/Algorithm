class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        map={}
        for i in range(len(isConnected)):
            map[i]=isConnected[i]
        visited=[False]*len(isConnected)
        cnt=0  
        def dfs(x):
            visited[x]=True
            for i in range(len(map[x])):
                if map[x][i]==0: continue
                if visited[i]: continue
                dfs(i)

        for i in range(len(isConnected)):
            if visited[i]: continue
            dfs(i)
            cnt+=1
        return cnt