#https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/
# Runtime: 6296 ms, faster than 5.02% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 40.2 MB, less than 31.29% of Python3 online submissions for Maximum Length of Repeated Subarray.
class Solution:
    def findLength(self,nums1, nums2) -> int:
        dp = [[None for _ in range(len(nums2))]
              for _ in range(len(nums1))]

        # base case
        if nums1[0]==nums2[0]:
            dp[0][0]=1
        else:
            dp[0][0]=0

        if nums1[0] in nums2:
            for j in range(1,len(nums2)):
                dp[0][j]=1
        else:
            for j in range(1,len(nums2)):
                dp[0][j]=0


        if nums2[0] in nums1:
            for i in range(1,len(nums1)):
                dp[i][0]=1
        else:
            for i in range(1,len(nums1)):
                dp[i][0]=0

        max_len = 0
        for i in range(1,len(nums1)):
            for j in range(1,len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i-1]==nums2[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else:
                        dp[i][j]=1
                else:
                    dp[i][j] = 0
                max_len = max(dp[i][j],max_len)
        return max_len