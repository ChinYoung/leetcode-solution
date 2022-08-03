#
# @lc app=leetcode.cn id=2050 lang=python3
#
# [2050] 并行课程 III
#

# @lc code=start
from cmath import cos
from typing import List


class Solution:
    def __init__(self) -> None:
        self.maxLog = {}

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if len(relations) == 0:
            return max(time)
        self.maxLog = {}
        res = self.buildGraph(n, relations, time)
        entries = res["entries"]
        costs = [self.getCost(entry) for entry in entries]
        return max(costs)

    def getCost(self, entry):
        index = entry.index
        costInLog = self.maxLog.setdefault(index, None)
        if costInLog:
            return costInLog
        cost = 0
        if len(entry.next) == 0:
            cost = entry.cost
        else:
            cost = entry.cost + max([self.getCost(node) for node in entry.next])
        self.maxLog[index] = cost
        return cost

    def buildGraph(self,n:int, relations: List[List[int]], time:List[int]):
        nodeMap = {}
        for i in range(n):
            index = i + 1
            cost = time[index - 1]
            node = Node(index, cost)
            nodeMap[index] = node
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
    print(s.minimumTime(1, [], [1]))
    print(s.minimumTime(3, [[2,3]], [3,1,1]))

