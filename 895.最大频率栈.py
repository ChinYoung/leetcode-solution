#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start


import collections


class FreqStack:
    def __init__(self):
        self.maxFreq = 0
        self.trace = collections.defaultdict(list)
        self.freqMap = collections.Counter()

    def push(self, val: int) -> None:
        newFreq = self.freqMap[val] + 1
        self.freqMap[val] = newFreq
        if self.freqMap[val] > self.maxFreq:
            self.maxFreq = self.freqMap[val]
        self.trace[newFreq].append(val)

    def pop(self) -> int:
        ele = self.trace[self.maxFreq].pop()
        self.freqMap[ele] -= 1
        if not self.trace[self.maxFreq]:
            self.maxFreq -= 1
        return ele
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
        print(s.pop())


