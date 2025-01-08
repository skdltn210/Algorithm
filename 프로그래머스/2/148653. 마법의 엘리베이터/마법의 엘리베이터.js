function solution(storey) {
  let ans = 0;
  let num = storey.toString().split("");

  for (let i = num.length - 1; i >= 0; i--) {
    let current = Number(num[i]);
    if (current < 5) {
      ans += current;
    } else if (current > 5) {
      ans += 10 - current;
      if (i > 0) num[i - 1] = Number(num[i - 1]) + 1;
      else ans++;
    } else {
      if (i === 0) {
        ans += 5;
      } else {
        if (num[i - 1] >= 5) {
          ans += 5;
          num[i - 1]++;
        } else {
          ans += 5;
        }
      }
    }
  }

  return ans;
}
