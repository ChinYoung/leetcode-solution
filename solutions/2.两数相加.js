/*
 * @lc app=leetcode.cn id=2 lang=javascript
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let root = new ListNode()
  let currentNode = root
  let carry = 0
  while (l1 || l2 || carry) {
    let v1 = l1 ? l1.val : 0
    let v2 = l2 ? l2.val : 0
    let value = v1 + v2 + carry
    if (value > 9) {
      carry = 1
      value = value - 10
    } else {
      carry = 0
    }
    currentNode.val = value
    l1 = l1 && l1.next
    l2 = l2 && l2.next
    if (l1 || l2 || carry) {
      let nextNode = new ListNode()
      currentNode.next = nextNode
      currentNode = nextNode
    }
  }
  return root
};
// @lc code=end

