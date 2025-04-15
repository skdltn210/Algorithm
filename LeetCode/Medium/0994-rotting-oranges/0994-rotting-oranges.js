/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let dx=[1,-1,0,0]
    let dy=[0,0,1,-1]
    let visited=Array(grid.length).fill(false).map(()=>Array(grid[0].length).fill(false))
    let queue=[]
    let cnt=0
    for(let i=0;i<grid.length;i++){
        for(let j=0;j<grid[0].length;j++){
            if(grid[i][j]===2) {
                queue.push([i,j])
                visited[i][j]=true
            } else if(grid[i][j]===0) visited[i][j]=true
        }
    }
    while(queue.length>0) {
        let len=queue.length
        for(let j=0;j<len;j++){
            [y,x]=queue.shift()
            visited[y][x]=true
            for(let i=0;i<4;i++){
                let ny=y+dy[i]
                let nx=x+dx[i]
                if(nx<0 || ny<0 || nx>=grid[0].length || ny>=grid.length) continue
                if(visited[ny][nx] || grid[ny][nx]===0) continue
                queue.push([ny,nx])
                visited[ny][nx]=true
            }
        }
        if(queue.length > 0) cnt+=1
    }
    if(visited.flat().flat().includes(false)) return -1
    return cnt
};