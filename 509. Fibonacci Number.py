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
            
# bottom up approach
#https://leetcode.com/problems/fibonacci-number/submissions/
#Runtime: 12 ms, faster than 95.10% of Python online submissions for Fibonacci Number.
#Memory Usage: 13.2 MB, less than 99.01% of Python online submissions for Fibonacci Number.
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            array = [None for _ in range(n+1)]
            array[0] = 0
            array[1] = 1
            for i in range(2,n+1):
                array[i] = array[i-1] + array[i-2]
            return array[n]                
