/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    let ans=[];
    function dfs(start,arr,sum) {
        if (arr.length===k && sum===n) {
            ans.push([...arr]);
            return;
        }
        
        if (arr.length>=k || sum>=n) {
            return;
        }
        
        for (let i=start; i<=9; i++) {
            arr.push(i);
            dfs(i+1,arr,sum+i);
            arr.pop(); 
        }
    }
    
    dfs(1,[],0);
    return ans;
};