#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
from typing import Dict, List


class FreqStack:
    def __init__(self):
        self.indexListMap = {}
        self.matrix = {}
        self.currentIndex = 0
        # TEST

    def push(self, val: int) -> None:
        # TEST

        indexList:List[int] = self.indexListMap.setdefault(val, [])
        currentTimes = len(indexList)
        nextTimes =currentTimes + 1

        indexList.append(self.currentIndex)
        self.currentIndex += 1

        currentRow = self.matrix.setdefault(currentTimes, {})
        nextRow = self.matrix.setdefault(nextTimes, {})
        try:
            del currentRow[val]
        except KeyError:
            pass
        if len(currentRow)==0:
            del self.matrix[currentTimes]
        nextRow[val] = True

        # TEST
        # print(' ', self.stack)

    def pop(self) -> int:
        maxCount = max(self.matrix.keys())
        currentRow:Dict[int:int] = self.matrix[maxCount]
        maxIndex = 0
        popELe = 0
        for val in currentRow.keys():
            indexList = self.indexListMap[val]
            for index in indexList:
                if index >= maxIndex:
                    maxIndex = index
                    popELe = val
        self.indexListMap[popELe].pop(-1)
        if len(self.indexListMap[popELe]) == 0:
            del self.indexListMap[popELe]
        if maxCount > 1:
            nextRow = self.matrix.setdefault(maxCount - 1, {})
            nextRow[popELe] = True
        del currentRow[popELe]
        if len(currentRow) == 0:
            del self.matrix[maxCount]
        return popELe

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end
if __name__ == "__main__":
    s = None
    eleList = [[],[5],[1],[2],[5],[5],[5],[1],[6],[1],[5],[],[],[],[],[],[],[],[],[],[]]
    # eleList = [[],[5],[1],[2],[5],[5],[5],[1],[6],[1],[5]]
    operaList = ["FreqStack","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
    for index, i in enumerate(eleList):
        if operaList[index] == 'FreqStack':
            s = FreqStack()
            continue
        if operaList[index] == 'push':
            s.push(i[0])
            continue
        s.pop()


