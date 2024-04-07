#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from utils import TreeUtils

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        node_stack = [[False, None, root, None, None]]
        while len(node_stack) != 0:
            is_left, parent_node, cur_node, max_val, min_val = node_stack[-1]
            if max_val != None and not cur_node.val < max_val:
                return False
            if min_val != None and not cur_node.val > min_val:
                return False
            if cur_node.left != None:
                node_stack.append([True, cur_node, cur_node.left, cur_node.val, min_val])
                cur_node = cur_node.left
            elif cur_node.right != None:
                node_stack.append([False, cur_node, cur_node.right, max_val, cur_node.val])
                cur_node = cur_node.right
            else:
                if is_left:
                    if parent_node != None:
                        parent_node.left = None
                    if len(node_stack) >= 2:
                        node_stack[-2][-1] = cur_node.val
                else:
                    if parent_node != None:
                        parent_node.right = None
                    if len(node_stack) >= 2:
                        node_stack[-2][-2] = cur_node.val
                node_stack.pop()
        return True
                
# @lc code=end

if __name__ == "__main__":
    s = Solution()

    # l = [5,1,4,None,None,3,6]
    # root = TreeUtils.list_to_tree(l)
    # print(s.isValidBST(root))

    # l = [2,1,3]
    # root = TreeUtils.list_to_tree(l)
    # print(s.isValidBST(root))

    # l = [5,4,6,None,None,3,7]
    # root = TreeUtils.list_to_tree(l)
    # print(s.isValidBST(root))

    l = [2,2,2]
    root = TreeUtils.list_to_tree(l)
    print(s.isValidBST(root))


