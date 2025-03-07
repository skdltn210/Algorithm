function solution(genres, plays) {
    const songs = []
    const map = new Map()
    for(let i=0;i<genres.length;i++){
        songs.push([genres[i],plays[i],i])
    }
    for(let song of songs){
        if(map.has(song[0])) map.set(song[0],map.get(song[0])+song[1])
        else map.set(song[0],song[1])
    }
    const genresWithPlay = [...map].sort((a,b) => (b[1]-a[1]))
    const ans = []
    songs.sort((a,b)=>(b[1]-a[1]))
    console.log(songs)
    console.log(genresWithPlay)
    for(let i=0;i<genresWithPlay.length;i++){
        for(let j=0;j<2;j++){
            for(let k=0;k<songs.length;k++){
                if(genresWithPlay[i][0] === songs[k][0] && !ans.includes(songs[k][2])) {
                    ans.push(songs[k][2])
                    break
                }
            }
        }
    }
    return ans
}