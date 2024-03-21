#
# @lc app=leetcode.cn id=2095 lang=python3
#
# [2095] 删除链表的中间节点
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        total = 1
        middle = 0
        cur = head
        middle_node = head
        prev = None
        while cur.next != None:
            cur = cur.next
            total+=1
            new_middle = int(total/2)
            if new_middle > middle:
                middle = new_middle
                prev = middle_node
                middle_node = middle_node.next
        prev.next = middle_node.next
        return head
            


# @lc code=end
if __name__ =="__main__":
    s = Solution()
    head = ListNode(1)
    cur = head
    for i in [2]:
        node = ListNode(i)
        cur.next = node
        cur = node
    head = s.deleteMiddle(head)
    while head.next != None:
        print(head.val)
        head = head.next
    print(head.val)

