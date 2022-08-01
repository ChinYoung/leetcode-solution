#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        res = self.buildGraph(relations, time)
        nodeMap = res["nodeMap"]
        entries = res["entries"]
        endPoints = res["endPoints"]

    def buildGraph(relations: List[List[int]], time:List[int]):
        nodeMap = {}
        for relation in relations:
            prevIndex = relation[0]
            nextIndex = relation[1]
            try:
                prevNode = nodeMap[prevIndex]
            except KeyError:
                cost = time[prevIndex - 1]
                prevNode = Node(prevIndex, cost)
                nodeMap[prevIndex] = prevNode
            try:
                nextNode = nodeMap[nextIndex]
            except KeyError:
                cost = time[nextIndex - 1]
                nextNode = Node(nextIndex, cost)
                nodeMap[nextIndex] = nextNode
            prevNode.next.append(nextNode)
            nextNode.prev.append(prevNode)
        entries = filter(lambda node: len(node.prev) == 0, nodeMap.values())
        endPoints = filter(lambda node: len(node.next) == 0, nodeMap.values())
        return {
            "nodeMap": nodeMap,
            "entries": entries,
            "endPoints": endPoints
        }

class Node:
    def __init__(self, index:int, cost:int) -> None:
        self.index = index
        self.cost = cost
        self.prev = []
        self.next = []
# @lc code=end

