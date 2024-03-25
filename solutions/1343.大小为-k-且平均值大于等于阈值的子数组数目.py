#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) <= k:
            return 1 if sum(arr)/k >= threshold else 0
        a = arr[:k]
        a_sum = sum(a)
        res = 1 if a_sum / k >= threshold else 0
        for i in range(k, len(arr)):
            in_num = arr[i]
            out_num = arr[i-k]
            a_sum = a_sum - out_num + in_num
            if a_sum/k >= threshold:
                res += 1
        return res

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    t = 4
    print(s.numOfSubarrays(arr, k, t))
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    t = 5
    print(s.numOfSubarrays(arr, k, t))

