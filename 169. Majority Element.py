
#https://leetcode.com/problems/majority-element/submissions/
#Runtime: 132 ms, faster than 86.10% of Python online submissions for Majority Element.
#Memory Usage: 14.7 MB, less than 68.35% of Python online submissions for Majority Element.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_dict = {num:0 for num in nums}
        maj = len(nums)//2+1
        for num in nums:
            element_dict[num] +=1
            if element_dict[num]>=maj:
                return num
            