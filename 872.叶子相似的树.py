#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafValueList(root1) == self.getLeafValueList(root2)

    def getLeafValueList(self, root: TreeNode):
        if root.left == None and root.right == None:
            return [root.val]
        left_list = [] if root.left == None else self.getLeafValueList(root.left)
        right_list = [] if root.right == None else self.getLeafValueList(root.right)
        return left_list + right_list
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    print(s.getLeafValueList(root))