function solution(rectangle, characterX, characterY, itemX, itemY) {
    const doubledRectangle = rectangle.map(r => [r[0]*2, r[1]*2, r[2]*2, r[3]*2]);
    const doubledCharacterX = characterX * 2;
    const doubledCharacterY = characterY * 2;
    const doubledItemX = itemX * 2;
    const doubledItemY = itemY * 2;
    
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;
    let ans = 0;
    
    for(let i = 0; i < doubledRectangle.length; i++){
        minX = Math.min(minX, doubledRectangle[i][0]);
        minY = Math.min(minY, doubledRectangle[i][1]);
        maxX = Math.max(maxX, doubledRectangle[i][2]);
        maxY = Math.max(maxY, doubledRectangle[i][3]);
    }
    
    let arr = Array(maxY + 1).fill(0).map(() => Array(maxX + 1).fill(0));
    
    for(let r of doubledRectangle){
        for(let i = r[1]; i <= r[3]; i++){
            for(let j = r[0]; j <= r[2]; j++){
                if(i === r[1] || i === r[3] || j === r[0] || j === r[2]) {
                    if(arr[i][j] === 0){
                        arr[i][j] = 1;
                    }
                }
                else {
                    arr[i][j] = 2;
                }
            }
        }
    }
    
    const bfs = (y, x) => {
        let dx = [0, 0, 1, -1];
        let dy = [1, -1, 0, 0];
        let queue = [[y, x]];
        let visited = Array(maxY + 1).fill(0).map(() => Array(maxX + 1).fill(false));
        visited[y][x] = true;
        
        while(queue.length > 0){
            let len = queue.length;
            for(let i = 0; i < len; i++){
                let curr = queue.shift();
                if(curr[0] === doubledItemY && curr[1] === doubledItemX) return ans / 2; 
                
                for(let j = 0; j < 4; j++){
                    let ny = curr[0] + dy[j];
                    let nx = curr[1] + dx[j];
                    if(nx < 0 || ny < 0 || ny >= arr.length || nx >= arr[0].length) continue;
                    if(arr[ny][nx] === 1 && !visited[ny][nx]) {
                        visited[ny][nx] = true;
                        queue.push([ny, nx]);
                    }
                }
            }
            ans++;
        }
        return -1; 
    }
    
    return bfs(doubledCharacterY, doubledCharacterX);
}