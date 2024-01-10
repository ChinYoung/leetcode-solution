import queue
from select import select
from typing import List


class Z_Heap:
    # (最大堆)节点比较方法, 可重写, 相等返回0, 胜出返回1, 否则返回-1
    @classmethod
    def compare(cls, first: int, second: int):
        if first == second:
            return 0
        return 1 if first > second else -1

    def __init__(self, nums: List[int]) -> None:
        self.__data = nums
        self.__heapify__()

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

    def __str__(self) -> str:
        return str(self.__data)
    
    # 从最后一个节点开始, 进行排序
    def __heapify__(self):
        if self.node_count < 2:
            return
        for i in reversed(range(self.node_count)):
            parent = self.__get_parent__(i)
            if parent != -1:
                self.__sift_down__(parent)

    def __switch__(self, first: int, second: int):
        self.__data[first], self.__data[second] = self.__data[second], self.__data[first]

    # 获取左子节点index
    def __get_left__(self, index: int):
        return 2 * index + 1

    # 获取右子节点index
    def __get_right__(self, index: int):
        return 2 * index + 2

    # 获取父节点index
    def __get_parent__(self, index: int):
        if index == 0:
            return -1
        return int((index - 1)/2)

    # 下沉操作
    # 先选出孩子节点中的较大值(最大堆为例), 与当前节点比较, 如果大于当前节点, 则交换位置, 并继续对被交换的孩子节点进行下沉
    def __sift_down__(self, index):
        left_index = self.__get_left__(index)
        right_index = self.__get_right__(index)
        if left_index > self.max_index:
            return
        to_compare = self.__data[left_index]
        to_compare_index = left_index
        # 比较左子节点和右子节点
        if right_index <= self.max_index:
            right_val = self.__data[right_index]
            if self.compare(right_val, to_compare) == 1:
                to_compare = right_val
                to_compare_index = right_index
        # 比较父节点和选出的子节点
        node_val = self.__data[index]
        if self.compare(to_compare, node_val) == 1:
            # 交换
            self.__switch__(to_compare_index, index)
            self.__sift_down__(to_compare_index)

    # 上浮操作
    # 与父节点比较, 如果大于父节点(最大堆为例), 则交换位置, 并在新的位置上继续进行上浮操作
    def __sift_up__(self, index):
        node_val = self.__data[index]
        parent_index = self.__get_parent__(index)
        if parent_index != -1:
            parent_val = self.__data[parent_index]
            if self.compare(node_val, parent_val) == 1:
                self.__switch__(parent_index, index)
                self.__sift_up__(parent_index)

    # 替换堆顶元素
    def replace(self, num):
        if self.node_count == 0:
            return
        replaced = self.__data[0]
        self.__data[0] = num
        self.__sift_down__(0)
        return replaced

    # 取出(删除并返回)堆顶节点
    # 将最小值(最大堆为例)与最大值交换, 弹出最大值, 然后对堆顶进行下沉操作
    def sift(self):
        if self.max_index == -1:
            raise Exception("empty heap")
        if self.max_index == 0:
            max = self.__data.pop()
            return max
        self.__switch__(0, self.max_index)
        max = self.__data.pop()
        self.__sift_down__(0)
        return max

    # 添加节点
    # 添加至队列末尾(堆的最远端), 然后进行上浮
    def insert(self, num):
        self.__data.append(num)
        self.__sift_up__(self.max_index)


# 最小堆
class A_Heap(Z_Heap):
    @classmethod
    def compare(cls, first: int, second: int):
        return super().compare(first, second) * -1


if __name__ == "__main__":
    list_o = [1, 2, 3, 44, 55, 66, 77, 33, 20, 12, 19, 35, 36, 21]
    a = A_Heap(list_o)
    print(a)
    z = Z_Heap(list_o)
    print(z)


