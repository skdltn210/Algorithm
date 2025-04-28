/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    let ans=[]
    let map=new Map()
    let graph=new Map()
    for(let i=0;i<equations.length;i++){
        let [x,y]=equations[i]
        map.set(`${x},${y}`,values[i])
        map.set(`${y},${x}`,1/values[i])
        if(!graph.has(x)) graph.set(x,[y])
        else graph.get(x).push(y)
        if(!graph.has(y)) graph.set(y,[x])
        else graph.get(y).push(x)
    }
    let visited, found;
    for(let query of queries){
        let [x,y] = query
        if(!graph.has(x) || !graph.has(y)) ans.push(-1)
        else if(x === y) ans.push(1)
        else if(map.has(`${x},${y}`)) ans.push(map.get(`${x},${y}`))
        else {
            visited=new Set()
            found=false
            let result=dfs(x,y,1)
            if(found) ans.push(result)
            else ans.push(-1)
        }
    }
    function dfs(current, target, product){
        if(current===target) {
            found=true
            return product
        }
        visited.add(current)
        for(let neighbor of graph.get(current)) {
            if(!visited.has(neighbor)) {
                let value = map.get(`${current},${neighbor}`)
                let res = dfs(neighbor, target, product * value)
                if(found) return res
            }
        }
        
        return -1
    }
    return ans
};