/*
 * @lc app=leetcode.cn id=26 lang=csharp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int? memoEle = null;
         int toFillIndex = 0;
         for (int i = 0; i < nums.Length; i++)
         {
             int currentEle = nums[i];
             if (currentEle != memoEle)
             {
                 nums[toFillIndex] = currentEle;
                 toFillIndex += 1;
                 memoEle = currentEle;
             }
         }
         return toFillIndex;
    }
}
// @lc code=end

