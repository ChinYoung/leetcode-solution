/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const map = {}
  const len = nums.length
  for (i = 0; i < len; i++) {
    let cur = nums.shift()
    if (map[cur] >= 0) {
      return [i, map[cur]]
    }
    map[target -cur] = i
  }
};
// @lc code=end

