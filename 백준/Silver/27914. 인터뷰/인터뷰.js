const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n, k, q;
let students = [];
let questions = [];
let lineCount = 0;

readline.on("line", (line) => {
  if (lineCount === 0) {
    [n, k, q] = line.split(" ").map(Number);
  } else if (lineCount === 1) {
    students = line.split(" ").map(Number);
  } else if (lineCount === 2) {
    questions = line.split(" ").map(Number);
    readline.close();
  }
  lineCount++;
});

readline.on("close", () => {
  solution();
  process.exit(0);
});

const solution = () => {
  for (let i = 0; i < questions.length; i++) {
    let cnt = 0;
    let q = questions[i];

    for (let l = 0; l < q; l++) {
      for (let j = l; j < q; j++) {
        let flag = 1;
        for (let m = l; m <= j; m++) {
          if (students[m] === k) {
            flag = 0;
            break;
          }
        }
        if (flag === 1) {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
};