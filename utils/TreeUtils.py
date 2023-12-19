from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(ele_list: List[int]) -> TreeNode:
    node_list = []
    max_index = len(ele_list) - 1
    for i in range(len(ele_list)):
        val = ele_list[i]
        if val == None:
            node_list.append(None)
            continue
        node_list.append(TreeNode(val))
    for i in range(len(ele_list)):
        if ele_list[i] == None:
            continue
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index <= max_index and node_list[left_index] != None:
            node_list[i].left = node_list[left_index]
        if right_index <= max_index and node_list[right_index] != None:
            node_list[i].right = node_list[right_index]
    return node_list[0]

def print_tree(root:TreeNode):
    current_list = [root]
    to_print = []
    while len(current_list) != 0:
        new_list = []
        level_to_print = []
        for i in current_list:
            level_to_print.append(i.val)
            left_node = i.left
            right_node = i.right
            print(i, left_node, right_node)
            if left_node == None and right_node == None:
                continue
            new_list.append(left_node if left_node != None else TreeNode(-1))
            new_list.append(right_node if right_node != None else TreeNode(-1))
        to_print.append(level_to_print)
        current_list = new_list
    print(to_print)
    max_to_print_len = len(to_print[-1])
    height = len(to_print)
    for e_list in to_print:
        blank_count = math.floor((max_to_print_len - len(e_list)))
        print(' ' * blank_count, end=' ' *  height)
        for i in e_list:
            print(i, end=' ')
        print()

if __name__ == '__main__':
    root = list_to_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    print_tree(root)