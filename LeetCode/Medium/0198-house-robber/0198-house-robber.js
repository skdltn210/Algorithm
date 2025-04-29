/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let n=nums.length
    if(n==1) return nums[0]
    if(n==2) return Math.max(nums[1],nums[0])
    dp=Array(n).fill(0)
    dp[0]=nums[0]
    dp[1]=nums[1]
    dp[2]=Math.max(dp[0]+nums[2],dp[1])
    for(let i=3;i<n;i++){
        dp[i]=Math.max(dp[i-1],dp[i-2]+nums[i],dp[i-3]+nums[i])
    }
    return dp[n-1]
};