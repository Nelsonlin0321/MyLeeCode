# https://leetcode.com/problems/two-sum/submissions/
# Runtime: 52 ms, faster than 16.65% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 9.80% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_dict = {target-num:i for (i,num) in enumerate(nums)}
        
        for i in range(len(nums)):
            
            if nums[i] in diff_dict:
                j = diff_dict[nums[i]]
                if i!=j:
                    return [i,j]
