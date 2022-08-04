#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# @lc code=end

