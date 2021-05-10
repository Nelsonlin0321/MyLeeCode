#https://leetcode.com/problems/longest-turbulent-subarray/submissions/ 
#Runtime: 488 ms, faster than 64.79% of Python3 online submissions for Longest Turbulent Subarray.
#Memory Usage: 18.7 MB, less than 40.84% of Python3 online submissions for Longest Turbulent Subarray.

class Solution:
    def maxTurbulenceSize(self, arr):
        dp = [None for _ in range(len(arr))]
        dp[0]=1
        
        if len(arr)==1:
            return 1
        
        if arr[0]==arr[1]:
            dp[1]=1
        else:
            dp[1]=2

        for i in range(2,len(arr)):
            if arr[i]==arr[i-1]: # 当前的值与上一个相同，当前的状态为1
                dp[i] = 1
            elif arr[i] < arr[i-1]:
                if arr[i-2]<arr[i-1]:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] =2
            elif arr[i] > arr[i-1]:
                if arr[i-2]>arr[i-1]:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] =2
        
        return max(dp)