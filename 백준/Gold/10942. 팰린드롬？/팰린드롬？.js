const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let line = 0;
const n = Number(input[line++]);
const arr = input[line++].split(" ").map(Number);
const m = Number(input[line++]);

let dp = Array.from(Array(n), () => Array(n).fill(0));

// 길이 1인 부분 수열은 모두 팰린드롬
for (let i = 0; i < n; i++) {
  dp[i][i] = 1;
}

// 길이 2인 부분 수열 확인
for (let i = 0; i < n - 1; i++) {
  if (arr[i] === arr[i + 1]) {
    dp[i][i + 1] = 1;
  }
}

// 길이 3 이상인 부분 수열
for (let len = 3; len <= n; len++) {
  for (let i = 0; i <= n - len; i++) {
    let j = i + len - 1;
    //양 끝이 같고 사이가 팰린드롬이면 팰린드롬임
    if (arr[i] === arr[j] && dp[i + 1][j - 1] === 1) {
      dp[i][j] = 1;
    }
  }
}

const result = [];
for (let i = 0; i < m; i++) {
  const [s, e] = input[line++].split(" ").map(Number);
  result.push(dp[s - 1][e - 1]);
}

console.log(result.join('\n'));