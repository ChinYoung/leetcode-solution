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
        entries = res["entries"]
        return max([self.getCost(entry) for entry in entries])

    def getCost(self, entry):
        if len(entry.next) == 0:
            return entry.cost
        return entry.cost + max([self.getCost(node) for node in entry.next])

    def buildGraph(self, relations: List[List[int]], time:List[int]):
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
        entries = [node for node in filter(lambda node: len(node.prev) == 0, nodeMap.values())]
        endPoints = [node for node in filter(lambda node: len(node.next) == 0, nodeMap.values())]
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

    def __str__(self) -> str:
        return "{}".format(self.cost)
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))
    print(s.minimumTime(3, [[1,3],[2,3]], [3,2,5]))

