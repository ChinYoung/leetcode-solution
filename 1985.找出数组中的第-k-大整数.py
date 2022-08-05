#
# @lc app=leetcode.cn id=1985 lang=python3
#
# [1985] 找出数组中的第 K 大整数
#

# @lc code=start
from typing import List

class Z_Heap:
    def __init__(self, nums: List[int]) -> None:
        self.__data = nums

    # 节点比较方法, 可重写, 相等返回0, 胜出返回1, 否则返回-1
    @classmethod
    def compare(cls, first:int, second:int):
        if first == second:
            return 0
        return 1 if first > second else -1

    @property
    def max_index(self):
        return len(self.__data) - 1

    @property
    def node_count(self):
        return len(self.__data)

    # 堆顶元素
    @property
    def best(self):
        return self.__data[0]

    # 获取左子节点index
    def get_left(self, index:int):
        return 2 * index + 1

    # 获取右子节点index
    def get_right(self, index:int):
        return 2 * index + 2

    # 获取父节点index
    def get_parent(self, index:int):
        if index == 0:
            return -1
        return int((index - 1)/2)

    # 从最后一个节点开始, 进行排序
    def heapify(self):
        if self.node_count < 2:
            return
        for i in reversed(range(self.node_count)):
            parent = self.get_parent(i)
            if parent != -1:
                self.sift_down(parent)

    # 下沉
    def sift_down(self, index):
        node_val = self.__data[index]
        left_index = self.get_left(index)
        if left_index > self.max_index:
            return
        comparing_val = self.__data[left_index]
        comparing_index = left_index
        right_index = self.get_right(index)
        if right_index <= self.max_index:
            right_val = self.__data[right_index]
            if self.compare(right_val, comparing_val) == 1:
                comparing_val = right_val
                comparing_index = right_index
        if self.compare(comparing_val, node_val) == 1:
            self.__data[comparing_index], self.__data[index] = self.__data[index], self.__data[comparing_index]
            self.sift_down(comparing_index)

    # 上浮
    def sift_up(self, index):
        node_val = self.__data[index]
        parent_index = self.get_parent(index)
        if parent_index != -1:
            parent_val = self.__data[parent_index]
            if self.compare(node_val, parent_val) == 1:
                self.__data[parent_index], self.__data[index] = self.__data[index], self.__data[parent_index]
                self.sift_up(parent_index)

    # 取出堆顶节点
    def sift(self):
        if self.max_index == -1:
            raise Exception("empty heap")
        if self.max_index == 0:
            max = self.__data.pop()
            return max
        self.__data[0], self.__data[self.max_index] = self.__data[self.max_index], self.__data[0]
        max = self.__data.pop()
        self.sift_down(0)
        return max

    # 替换堆顶元素
    def replace(self, num):
        if self.node_count == 0:
            return
        replaced = self.__data[0]
        self.__data[0] = num
        self.sift_down(0)
        return replaced

    # 添加节点
    def push(self, num):
        self.__data.append(num)
        self.sift_up(self.max_index)



class K_Heap(Z_Heap):
    @classmethod
    def compare(cls, first: str, second: str):
        if len(first) > len(second):
            return -1
        if len(first) < len(second):
            return 1
        for i in range(len(first)):
            num1 = int(first[i])
            num2 = int(second[i])
            if num1 > num2:
                return -1
            if num1 < num2:
                return 1
        return 0




class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        kh = K_Heap(nums[:k])
        kh.heapify()
        for i in nums[k:]:
            if kh.compare(i, kh.best) == -1:
                kh.replace(i)
        return kh.best

# @lc code=end

