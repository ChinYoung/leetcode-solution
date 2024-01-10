/*
 * @lc app=leetcode.cn id=3 lang=javascript
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  const len = s.length
  let start = 0
  let max = 0
  let char
  let container = {}
  let strLen
  let charIndex
  for (let i = 0; i < len; i++) {
      char = s[i]
      charIndex = container[char]
      if (charIndex !== undefined && charIndex >= start) {
          start = charIndex + 1
      }
      strLen = i - start + 1;
      (strLen > max) && (max = strLen);
      container[char] = i
  }
  return max
};
// @lc code=end

