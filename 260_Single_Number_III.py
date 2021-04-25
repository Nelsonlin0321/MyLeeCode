#https://leetcode.com/problems/single-number-iii/submissions/
#Runtime: 40 ms, faster than 89.36% of Python online submissions for Single Number III.
#Memory Usage: 15.7 MB, less than 22.34% of Python online submissions for Single Number III.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict = {value:0 for value in nums}
        for num in nums:
            num_dict[num]+=1
            if num_dict[num]>=2:
                del num_dict[num]
        return list(num_dict)