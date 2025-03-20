function solution(n, m, x, y, r, c, k) {
    let dx = [1, 0, 0, -1];
    let dy = [0, -1, 1, 0];
    let dir = ['d', 'l', 'r', 'u']; 
    const getManhattanDistance = (currX, currY) => {
        return Math.abs(r - currX) + Math.abs(c - currY);
    };
    
    const initialDistance = getManhattanDistance(x, y);
    
    if (initialDistance > k) return "impossible";
    
    if ((k - initialDistance) % 2 !== 0) return "impossible";
    
    const bfs = () => {
        let queue = [[x, y, ""]];
        
        for (let step = 0; step <= k; step++) {
            const size = queue.length;
            
            for (let i = 0; i < size; i++) {
                const [currX, currY, path] = queue.shift();
                
                if (currX === r && currY === c && path.length === k) {
                    return path;
                }
                
                const remainingMoves = k - path.length;
                
                const distanceToTarget = getManhattanDistance(currX, currY);
                
                if (distanceToTarget > remainingMoves) continue;
                
                if ((remainingMoves - distanceToTarget) % 2 !== 0) continue;
                
                for (let j = 0; j < 4; j++) {
                    const nx = currX + dx[j];
                    const ny = currY + dy[j];
                    
                    if (nx < 1 || ny < 1 || nx > n || ny > m) continue;
                    
                    const newPath = path + dir[j];
                    if (newPath.length <= k) {
                        queue.push([nx, ny, newPath]);
                    }
                }
            }
        }
        
        return "impossible"; 
    };
    
    return bfs();
}