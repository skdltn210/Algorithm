const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

readline
  .on("line", (line) => {
    input.push(line);
    readline.close();
  })
  .on("close", () => {
    solution(input[0]);
    process.exit();
  });

const solution = (input) => {
  const num = input.split("").map(Number);
  const len = input.length;
  let n = 1;
  let idx = 0;

  while (idx < len) {
    let curStr = n.toString();
    for (let i = 0; i < curStr.length; i++) {
      if (Number(curStr[i]) === num[idx]) {
        idx++;
        if (idx === len) break;
      }
    }
    n++;
  }
  console.log(n - 1);
};
