#
# @lc app=leetcode.cn id=2196 lang=python3
#
# [2196] 根据描述创建二叉树
#

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        rootMap = {}
        for desc in descriptions:
            parent = desc[0]
            child = desc[1]
            isLeft = desc[2]
            parentNode: TreeNode = nodeMap.setdefault(parent, TreeNode(parent))
            childNode: TreeNode = nodeMap.setdefault(child, TreeNode(child))
            rootMap.setdefault(parent, True)
            rootMap[child] = False
            # childNode.parent = parentNode
            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
            # if not parentNode.parent:
            #     root = parentNode
        for key in rootMap.keys():
            if rootMap[key]:
                return nodeMap[key]
        # tempQueue = [root]
        # valueList = []
        # while len(tempQueue) > 0:
        #     current = tempQueue.pop(0)
        #     valueList.append(current.val)
        #     if current.left:
        #         tempQueue.append(current.left)
        #     if current.right:
        #         tempQueue.append(current.right)
        # return valueList
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
