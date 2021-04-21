# https://leetcode.com/problems/two-sum/submissions/
#Runtime: 32 ms, faster than 73.37% of Python online submissions for Two Sum.
#Memory Usage: 13.5 MB, less than 76.25% of Python online submissions for Two Sum.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for (left_index,left_num) in enumerate(nums):
            for (right_index,right_num) in  enumerate(nums[left_index+1:]):
                if (left_num+right_num)==target:
                    return [left_index,right_index+left_index+1]