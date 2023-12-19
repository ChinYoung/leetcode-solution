#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#

from typing import Optional, List
from utils import TreeUtils

TreeNode = TreeUtils.TreeNode

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxPath = 0
        toCountList = [[root, True, True]]
        while len(toCountList) != 0:
            newToCount = []
            for i in toCountList:
                node, searchLeft, searchRight = i
                if searchLeft:
                    leftCount, leftForkList = self.generateLeftPath(node, True)
                    maxPath = max(maxPath, leftCount)
                    newToCount = newToCount + leftForkList
                if searchRight:
                    rightCount, rightForkList = self.generateRightPath(node, True)
                    maxPath = max(maxPath, rightCount)
                    newToCount = newToCount + rightForkList
            toCountList = newToCount
        return maxPath - 1

    def generateLeftPath(self, node: TreeNode, isRoot = False):
        curNodeCount = 1
        curForkList = [[node, False, True]] if node.right != None and not isRoot else []
        if node.left != None:
            nextCount, nextForkList = self.generateRightPath(node.left)
            return curNodeCount + nextCount, curForkList + nextForkList
        else:
            return curNodeCount, curForkList


    def generateRightPath(self, node: TreeNode, isRoot = False):
        curNodeCount = 1
        curForkList = [[node, True, False]] if node.left != None and not isRoot else []
        if node.right != None:
            nextCount, nextForkList = self.generateLeftPath(node.right)
            return curNodeCount + nextCount, curForkList + nextForkList
        else:
            return curNodeCount, curForkList

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.res = 0
#         self.traverse(root, 0, 0)
#         return self.res

#     def traverse(self, node, left, right):
#         if not node:
#             return
    
#         self.res = max(self.res, left, right)
#         self.traverse(node.left, 0, left+1)
#         self.traverse(node.right, right+1, 0)

# @lc code=end

if __name__ == '__main__':
    value_list = [10,7,10,7,6,2,5,3,4,6,2,7,7,9,None,69,5,7,5,None,None,5,5,2,5,1,None,None,2,10,4,3,None,4,1,None,2,6,None,3,8,None,2,7,1,None,None,None,None,10,10,4,2,None,None,10,1,None,1,None,None,None,None,None,3,None,None,3,4,None,8,None,6,6,10,8,None,4,2,10,10,9,7,10,1,None,9,None,None,4,None,None,None,4,None,None,None,9,None,5,2,3,2,10,9,None,7,None,1,4,None,3,None,None,9,None,None,None,None,None,None,None,None,None,None,1,2,None,4,None,None,6,None,6,6,None,None,None,None,1,None,None,None,2,8,None,None,None,None,5,8,4,2,None,None,None,None,6,9,5,5,None,None,5,None,1,2,None,None,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None,4,None,None,6,None,3,None,None,None,1,2]
    # value_list = [1,1,1,None,1,None,None,None,None,1,1,None,None,None,None,None,None,None,None,None,1]
    root: TreeNode = TreeUtils.list_to_tree(value_list)
    TreeUtils.print_tree(root)
    s = Solution()
    print(s.longestZigZag(root))





