/*
 * @lc app=leetcode.cn id=953 lang=javascript
 *
 * [953] 验证外星语词典
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
  for (let i = 0; i < words.length - 1;i++) {
    const first = words[i]
    const second = words[i+1]
     for (let j = 0; j < Math.max(first.length, second.length);j++) {
        const firstIndex = order.indexOf(first[j])
        const secondIndex = order.indexOf(second[j])
        if (firstIndex < secondIndex) {
            break
        }
        if (firstIndex > secondIndex) {
            return false
        }

    }
  }
  return true
};
// @lc code=end

