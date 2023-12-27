from typing import List
import math
#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, direction = self.move(0, 0, 'N', instructions)
        equivalentMove = self.toEquivalent(x, y, direction)
        # print(x, y, direction)
        # print(equivalentMove)
        for i in range(3):
            x, y, direction = self.move(x,y, direction,equivalentMove)
        #     print(x, y, direction)
        # print(x, y)
        return x == 0 and y == 0
    
    def move(self, x: int, y: int, direction: str, instructions: str):
        for i in instructions:
            # print(i, x, y, direction)
            if i == "G":
                if direction == 'N':
                    y+=1
                elif direction == 'S':
                    y-=1
                elif direction == 'E':
                    x+=1
                elif direction == 'W':
                    x-=1
            elif i=='L':
                if direction == "N":
                    direction = 'W'
                elif direction == 'W':
                    direction = 'S'
                elif direction == 'S':
                    direction = 'E'
                elif direction == 'E':
                    direction = 'N'
            elif i=='R':
                if direction == "N":
                    direction = 'E'
                elif direction == 'W':
                    direction = 'N'
                elif direction == 'S':
                    direction = 'W'
                elif direction == 'E':
                    direction = 'S'
        return x, y, direction

    def toEquivalent(self, x: int, y: int, direction: str):
        if x ==0 and y == 0:
            return ''
        res = ''
        firstMove = abs(y) * 'G'
        secondMove = abs(x) * 'G'
        firstReDirect = ''
        secondReDirect = ''
        directionAfterMove = 'N'
        finalRedirect = ''
        # first redirect
        if y >= 0:
            pass
        elif y < 0:
            firstReDirect = 'LL'
            directionAfterMove = 'S'
        # second redirect
        if y > 0:
            if x > 0:
                secondReDirect = 'R'
                directionAfterMove = 'E'
            if x < 0:
                secondReDirect = 'L'
                directionAfterMove = 'W'
        elif y < 0:
            if x > 0:
                secondReDirect = 'L'
                directionAfterMove = 'E'
            if x < 0:
                secondReDirect = 'R'
                directionAfterMove = 'W'
        elif y == 0:
            if x > 0:
                secondReDirect = 'R'
                directionAfterMove = 'E'
            if x < 0:
                secondReDirect = 'L'
                directionAfterMove = 'W'
        # final redirect
        if directionAfterMove == 'N':
            if direction == 'N':
                pass
            elif direction == 'S':
                finalRedirect = 'LL'
            elif direction == 'E':
                finalRedirect = 'R'
            elif direction == 'W':
                finalRedirect = 'L'
        elif directionAfterMove == 'S':
            if direction == 'N':
                finalRedirect = 'LL'
            elif direction == 'S':
                pass
            elif direction == 'E':
                finalRedirect = 'L'
            elif direction == 'W':
                finalRedirect = 'E'
        elif directionAfterMove == 'E':
            if direction == 'N':
                finalRedirect = 'L'
            elif direction == 'S':
                finalRedirect = 'R'
            elif direction == 'E':
                pass
            elif direction == 'W':
                finalRedirect = 'LL'
        elif directionAfterMove == 'W':
            if direction == 'N':
                finalRedirect = 'R'
            elif direction == 'S':
                finalRedirect = 'L'
            elif direction == 'E':
                finalRedirect = 'LL'
            elif direction == 'W':
                pass
        return firstReDirect + firstMove + secondReDirect + secondMove + finalRedirect

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.isRobotBounded('GGLLGG'))
    print(s.isRobotBounded('GG'))
    print(s.isRobotBounded('GL'))
    print(s.isRobotBounded('LLGRL'))

