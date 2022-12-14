#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.searchNode(root, p.val)
        # 找出到 p 的 path 后, 从最大深度的节点开始, 检查是否能找到到 q 的路径, 如果可以找到, 则该 node 为公共祖先
        while len(pPath) > 0:
            pathNode = pPath.pop(len(pPath)-1)
            ancestor = pathNode
            if self.searchNode(pathNode, q.val):
                return ancestor
        return ancestor

    # 找出从 root, 开始到指定值的路径, 从左到右对应从上到下的顺序
    def searchNode(self, root:TreeNode, val):
        current = root
        searchStack = []
        searchLog = {}
        while current:
            if current.val == val:
                searchStack.append(current)
                return searchStack
            searchLog[current.val] = True
            if current.left and not searchLog.setdefault(current.left.val, False):
                searchStack.append(current)
                current = current.left
                continue
            if current.right and not searchLog.setdefault(current.right.val, False):
                searchStack.append(current)
                current = current.right
                continue
            try:
                current = searchStack.pop(len(searchStack) - 1)
            except IndexError:
                return None


# @lc code=end
# 从 List 生成二叉树
def generateTree(all:List[int]):
    root:TreeNode = None
    nodeMap ={}
    maxIndex = len(all) - 1
    for index,i in enumerate(all):
        node = nodeMap.setdefault(index, TreeNode(i))
        if index == 0:
            root = node
        leftIndex = 2 * index + 1
        if leftIndex <= maxIndex:
            leftValue = all[leftIndex]
            if leftValue != None:
                leftNode = TreeNode(leftValue)
                nodeMap[leftIndex] = leftNode
                node.left = leftNode
        rightIndex = 2 * index + 2
        if rightIndex <= maxIndex:
            rightValue = all[rightIndex]
            if rightValue != None:
                rightNode = TreeNode(rightValue)
                nodeMap[rightIndex] = rightNode
                node.right = rightNode
    return root

# 依照广度优先的顺序print一棵树
def bfsPrint(root:TreeNode):
    nodeQueue = [root]
    current = None
    while len(nodeQueue) > 0:
        current = nodeQueue.pop(0)
        print(current.val)
        if current.left:
            nodeQueue.append(current.left)
        if current.right:
            nodeQueue.append(current.right)

# 根据值获取树中的某个节点
def getNode(root, val):
    nodeStack = [root]
    current:TreeNode = None
    while len(nodeStack) > 0:
        current = nodeStack.pop(0)
        if current.val == val:
            return current
        if current.left:
            nodeStack.append(current.left)
        if current.right:
            nodeStack.append(current.right)
    return None

# 格式化 print 栈, 栈顶在 List 尾
def printStack(stack:List[TreeNode]):
    print('[', end='')
    for i in stack:
        print(i.val, end=',')
    print(']', end='\n')

if __name__ =="__main__":
    all = [3,5,1,6,2,0,8,None,None,7,4]
    root = generateTree(all)
    # bfsPrint(root)
    p = getNode(root, 7)
    q = getNode(root, 4)
    s = Solution()
    print(s.lowestCommonAncestor(root,p, q).val)

