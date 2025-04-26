/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let max=0
    for(let pile of piles){
        max=Math.max(max,pile)
    }
    let left=1
    let right=max

    const time = (mid) => {
        let num=0
        for(let pile of piles){
            num+=Math.ceil(pile/mid)
        }
        return num
    }

    while(left<=right){
        let mid=Math.floor((left+right)/2)
        if(time(mid)<=h){
            right=mid-1
        } else{
            left=mid+1
        }
    }
    return left
};