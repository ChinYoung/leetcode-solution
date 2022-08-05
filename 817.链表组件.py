#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        r = 0
        keep = 0
        while head:
            if head.val in nums:
                if not keep:
                    r += 1
                    keep = 1
            else:
                keep = 0
            head = head.next
        return r
# @lc code=end

