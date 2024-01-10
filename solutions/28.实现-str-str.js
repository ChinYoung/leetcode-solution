/*
 * @lc app=leetcode.cn id=28 lang=javascript
 *
 * [28] 实现 strStr()
 */

// @lc code=start
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  if (!needle.length) {
    return 0
  }
  let index = 0
  let needleLen = needle.length
  let haystackLen = haystack.length
  while(true) {
      if(haystack.slice(index, index + needleLen) === needle) {
          return index
      }
      if (index > (haystackLen - needleLen)) {
          return -1
      }
      index = index + 1
  }
};
// @lc code=end

