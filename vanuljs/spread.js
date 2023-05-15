const arr = [2, 5, -1, 7, 3, 1];
const max = Math.max(...arr);
const wrong_max = Math.max(arr);

console.log(max);
// 7
console.log(wrong_max);
// NaN
