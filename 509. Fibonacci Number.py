#https://leetcode.com/problems/fibonacci-number/submissions/
#Runtime: 1368 ms, faster than 5.05% of Python online submissions for Fibonacci Number.
#Memory Usage: 13.3 MB, less than 63.70% of Python online submissions for Fibonacci Number.
class Solution(object):
    def __init__(self):
        self.array = [-1 for _ in range(31)]
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
            if self.array[n]==-1:
                return self.fib(n-1)+self.fib(n-2)
            else:
                return self.array[n]