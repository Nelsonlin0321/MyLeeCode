#https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/submissions/
#Runtime: 56 ms, faster than 66.67% of Python online submissions for Minimum Moves to Equal Array Elements II.
#Memory Usage: 14.6 MB, less than 54.39% of Python online submissions for Minimum Moves to Equal Array Elements II.
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)%2==0:
            mid = (nums[len(nums)//2-1] + nums[len(nums)//2])//2
        else:
            mid  = nums[len(nums)//2]
            
        cnt = 0
        for num in nums:
            cnt += abs(num-mid)
        return cnt