function solution(plans) {
    var answer = []
    var stop = []
    for(plan of plans){
        var time = Number(plan[1].substr(0,2))*60 + Number(plan[1].substr(3,5));
        plan[1] = time
        plan[2] = Number(plan[2])
    }
    plans.sort((a,b)=>a[1]-b[1])
    for(let i=0;i<plans.length-1;i++){
        time = plans[i][1]+plans[i][2]-plans[i+1][1]
        if(time<=0){
            answer.push(plans[i][0])
            while(stop.length>0){
                if(stop[stop.length-1][2]+time>0){
                    stop[stop.length-1][2]+=time
                    break
                }
                else{
                    time+=stop[stop.length-1][2]
                    answer.push(stop.pop()[0])
                }
            }
        }
        else {
            plans[i][2] = time
            stop.push(plans[i])
        }
    }
    answer.push(plans[plans.length-1][0])
    while(stop.length>0){
        answer.push(stop.pop()[0])
    }
    return answer;
}