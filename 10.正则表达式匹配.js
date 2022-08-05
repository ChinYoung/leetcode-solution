/*
 * @lc app=leetcode.cn id=10 lang=javascript
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
  if (!s && !p)  {
    return true
  }
  let pIndex = 0
  let pList = {}
  while (pIndex < p.length) {
    if (p[pIndex + 1] !== '*') {
      pList[`${pIndex}-${p[pIndex]}`] = false
      pIndex = pIndex + 1
    } else {
      pList[`${pIndex}-${p[pIndex]}-*`] = true
      pIndex = pIndex + 2
    }
  }
  let pointerList = [0]
  let pattern = ''
  patternList = Object.keys(pList)
  let endMatch = false
  let leftAllTrue = true
  patternList.forEach((i, index) => {
    leftAllTrue = patternList.slice(index + 1).reduce((final, key) => final && !!pList[key], true)
    let newList = []
    pattern = i.split('-')[1]
    if (i.slice(-1) !== '*') {
      pointerList.forEach(j => {
        const value = s[j]
        if (value && (value === pattern || pattern === '.')) {
          if ( j >= s.length - 1 && leftAllTrue) {
            endMatch = true
          }
          pList[i] = true
          if (j < s.length - 1) {
            newList.push(j + 1)
          }
        }
      })
      pointerList = newList
    }
    if (i.slice(-1) === '*') {
      newList = pointerList
      if (index === patternList.length - 1 && (!pointerList.length || !s.length)) {
        endMatch = true
      }
      pointerList.forEach(pointer => {
        let current = pointer
        let next
        while (s[current] === pattern || pattern === '.') {
          if (current >= s.length - 1 && leftAllTrue) {
            endMatch = true
          }
          next = current + 1
          if (next < s.length && newList.indexOf(next) === -1) {
            newList.push(next)
            current = next
          } else {
            break
          }
        }
      })
      pointerList = newList
    }
  })
  return endMatch && Object.keys(pList).reduce((final, key) => final && !!pList[key], true)
};
// @lc code=end

