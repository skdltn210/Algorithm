const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n;

readline
  .on("line", (line) => {
    n = parseInt(line);
    readline.close();
  })
  .on("close", () => {
    solution();
    process.exit();
  });

const solution = () => {
  let dp = [0, 1, 2];
  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
  }
  console.log(dp[n]);
};
