#https://leetcode.com/problems/longest-continuous-increasing-subsequence/submissions/
#Runtime: 64 ms, faster than 97.50% of Python3 online submissions for Longest Continuous Increasing Subsequence.
#Memory Usage: 15.5 MB, less than 16.79% of Python3 online submissions for Longest Continuous Increasing Subsequence.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        dp = [None for _ in  range(len(nums))]
        dp[0] = 1
        for index in range(1,len(nums)):

            if nums[index]>nums[index-1]:
                dp[index] = dp[index-1]+1
            else:
                dp[index] = 1
        return max(dps)