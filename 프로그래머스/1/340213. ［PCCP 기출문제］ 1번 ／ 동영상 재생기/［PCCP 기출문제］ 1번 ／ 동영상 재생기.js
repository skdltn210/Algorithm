function timeToMin(time){
    return parseInt(time.split(':')[0])*60 + parseInt(time.split(':')[1])
}

function minToTime(min){
    let hour = Math.floor(min/60)
    let minute = min%60

    return (hour < 10 ? '0' + hour : hour) + ':' + (minute < 10 ? '0' + minute : minute);
}

function solution(video_len, pos, op_start, op_end, commands) {
    let totalMin = timeToMin(video_len)
    let posMin = timeToMin(pos)
    let startMin = timeToMin(op_start)
    let endMin = timeToMin(op_end)
    if(posMin>=startMin && posMin <=endMin){
            posMin = endMin
        }
    for(command of commands){
        if(command === 'prev'){
            if(posMin<10){
                posMin=0;
            }
            else posMin-=10;
        }
        else if(command === 'next'){
            if(posMin+10>totalMin){
                posMin = totalMin;
            }
            else posMin+=10;
        }
        if(posMin>=startMin && posMin <=endMin){
            posMin = endMin
        }
    }
    return minToTime(posMin);
}