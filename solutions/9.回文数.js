/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  if (x.length === 1) {
    return true
  }
  const str = x + ''
  const list = Array.from(str)
  let lindex = 0
  let rindex = list.length - 1
  let isPalindrome = true
  while (rindex > lindex) {
    isPalindrome = (list[lindex] === list[rindex])
    if (!isPalindrome) {
      break
    }
    lindex = lindex + 1
    rindex = rindex - 1
  }
  return isPalindrome
};
// @lc code=end

