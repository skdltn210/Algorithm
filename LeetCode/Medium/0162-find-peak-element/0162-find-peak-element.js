/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let arr=[]
    for(let i=0;i<nums.length;i++){
        arr.push([i,nums[i]])
    }
    arr.sort((a,b)=>b[1]-a[1])
    return arr[0][0]
    // let left=0
    // let right=arr.length-1

    // while(left<right){
    //     let mid=Math.floor((left+right)/2)
    // }
};