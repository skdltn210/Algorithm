function solution(targets) {
    var answer = 0;
    var x=0
    targets.sort((a,b) => a[1]-b[1])
    for(let i=0;i<targets.length;i++){
        if(x<=targets[i][0]){
            x=targets[i][1]
            answer+=1
        }
    }
    return answer;
}