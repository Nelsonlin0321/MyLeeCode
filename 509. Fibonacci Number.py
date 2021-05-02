#https://leetcode.com/problems/fibonacci-number/submissions/
#Runtime: 12 ms, faster than 95.10% of Python online submissions for Fibonacci Number.
#Memory Usage: 13.4 MB, less than 63.70% of Python online submissions for Fibonacci Number.
class Solution(object):
    def __init__(self):
        self.array = [None for _ in range(31)]
        self.array[0] = 0
        self.array[1] = 1
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return self.array[n]
        else:
            if self.array[n] is None:
                result =  self.fib(n-1)+self.fib(n-2)
                # memory the result!
                self.array[n]=result
                return result
            else:
                return self.array[n]
