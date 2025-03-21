function solution(stones, k) {
    const arr = new Array(stones.length);
    let front = 0;  
    let rear = 0;  
    for(let i=0; i<k; i++){
        while (front < rear && stones[arr[rear-1]] <= stones[i]) {
            rear--;
        }
        arr[rear++] = i;
    }
    
    let ans = stones[arr[front]];
    
    for(let i=k; i<stones.length; i++){
        if(arr[front] <= i-k) {
            front++;  
        }
        
        while (front < rear && stones[arr[rear-1]] <= stones[i]) {
            rear--;
        }
        arr[rear++] = i;
        
        ans = Math.min(ans, stones[arr[front]]);
    }
    
    return ans;
}