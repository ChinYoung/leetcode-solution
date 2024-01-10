#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from importlib.resources import path
import math
from typing import Dict, List


class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.count = 0
        self.testAllLists(root, 0)
        return self.count

    def testAllLists(self, node:TreeNode, pathVal):
        val = node.val
        pathVal = pathVal ^ int(math.pow(2, val-1))
        if not (node.left or node.right):
            if pathVal == 0 or (pathVal in [1,2,4,8,16,32,64,128,256]):
                self.count += 1
        if node.left:
            self.testAllLists(node.left, pathVal)
        if node.right:
            self.testAllLists(node.right, pathVal)
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome([1,1,1,7,7]))


