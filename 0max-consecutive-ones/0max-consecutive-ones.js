/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var ans=0
    for(var i=0;i<nums.length;i++){
        if(nums[i]==1){
            var cnt=1
            for(var j=i+1;j<nums.length;j++){
                if(nums[j]==1){
                    cnt+=1
                }
                else{
                    if(cnt>ans){
                        ans=cnt
                    }
                    break
                }
            }
            if(cnt>ans){
                ans=cnt
            }
        }
        
    }
    return ans
};