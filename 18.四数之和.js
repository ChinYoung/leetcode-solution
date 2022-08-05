/*
 * @lc app=leetcode.cn id=18 lang=javascript
 *
 * [18] 四数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
  const len = nums.length
  let sorted = nums.sort((p, c) => p - c)
  const max = sorted[len -1]
  const min = sorted[0]
  const res = []
  const container = {}
  sorted = sorted.filter(i => !(i + 3 * max < target || i + 3 * min > target))
  sorted.forEach((i, indexI) => {
    if (container[i]) {
      return
    }
    container[i] = {}
    const left1 = sorted.slice(indexI + 1).filter(j => !(i + j + 2 * max < target || i + j + 2 * min > target))
    left1.forEach((j, indexJ) => {
      if (container[i][j]) {
        return
      }
      container[i][j] = {}
      const left2 = left1.slice(indexJ + 1).filter(k => !(i + j + k + max < target || i + j + k + min > target))
      left2.forEach((k, indexK) => {
        if (container[i][j][k]) {
          return
        }
        container[i][j][k] = {}
        const left3 = left2.slice(indexK + 1)
        left3.forEach((l) => {
          if (container[i][j][k][l] !== undefined || i + j + k + l !== target) {
            return
          }
          container[i][j][k][l] = l
          res.push([
            i, j, k, l
          ])
        })
      })
    })
  })
  return res
};
// @lc code=end

