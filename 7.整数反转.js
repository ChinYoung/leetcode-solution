/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  if (!x) {
    return x
  }
  let temp = []
  const s = x + ''
  Array.from(s).forEach(i => {
    temp.unshift(i)
  })
  const num = parseInt(temp.join(''))
  const maxValue = Math.pow(2, 31)
  if (num < maxValue * -1 || num > maxValue -1) {
    return 0
  }
  return num * x / Math.abs(x)
};
// @lc code=end

