#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        leftList = []
        rightList = []
        rootList = [root.val]
        if root.left:
            leftList = self.preorderTraversal(root.left)
            rootList.extend(leftList)
        if root.right:
            rightList = self.preorderTraversal(root.right)
            rootList.extend(rightList)
        return rootList
# @lc code=end

