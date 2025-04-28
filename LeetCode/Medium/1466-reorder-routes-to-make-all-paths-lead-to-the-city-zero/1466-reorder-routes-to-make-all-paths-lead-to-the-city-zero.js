/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    let map = new Map()
    let set = new Set()
    let visited=new Set()
    let cnt=0
    for(let i=0;i<n;i++) map.set(i,[])
    for(let connection of connections){
        [i,j]=connection
        map.get(i).push(j)
        map.get(j).push(i)
        set.add(`${i},${j}`)
    }
    const dfs = (x) => {
        visited.add(x)
        for(let i of map.get(x)){
            if(!visited.has(i)){
                if(set.has(`${x},${i}`)) cnt++
                dfs(i)
            }
        }
    }
    dfs(0)
    return cnt
};