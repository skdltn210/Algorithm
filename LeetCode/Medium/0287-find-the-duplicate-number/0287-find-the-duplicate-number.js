/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    nums.sort((a,b) => a-b)
    prev=nums[0]
    for(let i=1;i<nums.length;i++){
        if(prev===nums[i]) return prev
        prev=nums[i]
    }
};