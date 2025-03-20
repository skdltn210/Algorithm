function solution(price, money, count) {
    let m=0
    for(let i=0;i<count;i++) m+=price*(i+1)
    if(m-money<=0) return 0
    return m-money
}