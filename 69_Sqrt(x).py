#Runtime: 24 ms, faster than 58.13% of Python online submissions for Sqrt(x).
#Memory Usage: 13.3 MB, less than 89.82% of Python online submissions for Sqrt(x).

class Solution(object):
    
    def select_middle(self,start,end):
        if start ==end:
            return middle
        else:
            middle  = start + (end-start)//2
            return middle 
        
    def mySqrt(self,x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x

        start = 1
        end = x-1
        while (end-start>1):
            middle = self.select_middle(start,end)
            if middle**2> x:
                end = middle
            elif middle**2<x:
                start = middle
            else:
                return middle

        return start

solution = Solution()
solution.mySqrt(2147395599)