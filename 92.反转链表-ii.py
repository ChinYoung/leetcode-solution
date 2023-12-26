#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        curIndex = 1
        leftEnd = None
        reverseStart = None
        prev = None
        if left == right or head.next == None:
            return head
        while cur != None:
            if curIndex < left:
                prev = cur
                cur = cur.next
                curIndex += 1
                continue
            if curIndex == left:
                leftEnd = prev
                reverseStart = cur
                prev = cur
                cur = cur.next
                curIndex += 1
                continue
            if curIndex > left and curIndex <right:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                curIndex += 1
                continue
            if curIndex == right:
                if leftEnd != None:
                    leftEnd.next = cur
                else:
                    head = cur
                reverseStart.next = cur.next
                cur.next = prev
                return head
        return head

# @lc code=end
    

if __name__ =="__main__":
    s = Solution()
    head = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_7 = ListNode(7)
    node_8 = ListNode(8)
    head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8

    res = s.reverseBetween(head, 2, 4)
    print(res.val)
    while res.next != None:
        print(res.next.val)
        res = res.next

