#
# @lc app=leetcode.cn id=2385 lang=python3
#
# [2385] 感染二叉树需要的总时间
#

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class LinkParentNode(TreeNode):
    def __init__(self, val=0, left=None, right=None, parent=None):
        super().__init__(val, left, right)
        self.parent = parent
        self.infected = False

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        linked_root = self.linkParent(root)
        first_node = self.find_by_val(linked_root, start)
        times = 0
        next_list = [first_node]
        while True:
            new_list = []
            for i in next_list:
                i.infected = True
                if i.parent and not i.parent.infected:
                    new_list.append(i.parent)
                if i.left and not i.left.infected:
                    new_list.append(i.left)
                if i.right and not i.right.infected:
                    new_list.append(i.right)
            next_list = new_list
            if len(new_list) == 0:
                return times
            times += 1

        # self.printTree([linked_root])
        # print()
        # print(self.find_by_val(linked_root, 4).val)
        # print(self.find_by_val(linked_root, 3).left.val)

    def linkParent(self, node: TreeNode, parent = None):
        linked_root = LinkParentNode(node.val, node.left, node.right, parent)
        if node.left:
            linked_root.left = self.linkParent(linked_root.left, linked_root)
        if node.right:
            linked_root.right = self.linkParent(linked_root.right, linked_root)
        return linked_root

    def printTree(self, nodes: List[LinkParentNode]):
        sub_list = []
        for i  in nodes:
            print(i.val, sep=" ", end=" ")
            if i.left:
                sub_list.append(i.left)
            if i.right:
                sub_list.append(i.right)
        print()
        if len(sub_list):
            self.printTree(sub_list)

    def find_by_val(self, root: LinkParentNode, value: int):
        node_list = [root]
        while len(node_list) != 0:
            target_node = self.find(node_list, value)
            if target_node != None:
                return target_node
            new_list = []
            for i in node_list:
                if (i.left):
                    new_list.append(i.left)
                if (i.right):
                    new_list.append(i.right)
            node_list = new_list

    def find(self, node_list: List[LinkParentNode], value: int):
        for i in node_list:
            if i.val == value:
                return i
        return None



        
# @lc code=end

if __name__ == '__main__':
    node_9 = TreeNode(9)
    node_2 = TreeNode(2)
    node_10 = TreeNode(10)
    node_6 = TreeNode(6)
    node_4 = TreeNode(4, node_9, node_2)
    node_3 = TreeNode(3, node_10, node_6)
    node_5 = TreeNode(5, None, node_4)
    root = TreeNode(1, node_5, node_3)
    s = Solution()
    print(s.amountOfTime(root, 3))

    root_1 = TreeNode(1)
    print(s.amountOfTime(root_1, 1))


