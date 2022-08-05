#
# @lc app=leetcode.cn id=1970 lang=python3
#
# [1970] 你能穿过矩阵的最后一天
#

# @lc code=start
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cellMap = {}
        for index, cell in enumerate(cells):
            rowVal = cell[0]
            colVal = cell[1]
            node = CellNode(cell, index)
            node.root = node
            node.mostRight = node
            node.subNodes = [node]
            rowMap = cellMap.setdefault(rowVal, {})
            rowMap[colVal] = node
            mostLeft = node.root
            allTree = [node.root]
            linkedNodes = self.getLinkedNodes(node, cellMap)
            for linkedNode in linkedNodes:
                if not linkedNode.root in allTree:
                    allTree.append(linkedNode.root)
                if linkedNode.root.col < mostLeft.col:
                    mostLeft = linkedNode.root
            for treeRoot in allTree:
                if treeRoot != mostLeft:
                    for sub in treeRoot.subNodes:
                        sub.root = mostLeft
                    mostLeft.subNodes.extend(treeRoot.subNodes)
                    if treeRoot.mostRight.col > mostLeft.mostRight.col:
                        mostLeft.mostRight = treeRoot.mostRight
            if abs(mostLeft.mostRight.col - mostLeft.col) == (col - 1):
                return index
        return len(cells)

    def getLinkedNodes(self, node, cellMap):
        linkedNodes = []
        for delta in [[0,1], [0,-1],[1,1],[1,0],[1,-1],[-1,0],[-1,1],[-1,-1]]:
            newRow = node.row + delta[0]
            newCol = node.col + delta[1]
            try:
                linkedNode = cellMap[newRow][newCol]
                linkedNodes.append(linkedNode)
            except KeyError:
                pass
        return linkedNodes

class CellNode:
    def __init__(self, cell:List[int], index: int):
        self.index = index
        self.cellValue = cell
        self.row = cell[0]
        self.col = cell[1]
        self.id = "{},{}".format(cell[0], cell[1])
        self.root = None
        self.mostRight = None
        self.subNodes = []

    def __str__(self):
        return self.id
# @lc code=end

