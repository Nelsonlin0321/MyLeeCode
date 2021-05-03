#https://leetcode.com/problems/perfect-squares/submissions/
#Runtime: 5204 ms, faster than 18.06% of Python3 online submissions for Perfect Squares.
#Memory Usage: 14.3 MB, less than 74.78% of Python3 online submissions for Perfect Squares.
class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo_list = [None for _ in range(n+1)]
        memo_list[0] = 0
        
        for i in range(1,n+1):
            print
            memo_list[i] = float("inf")
            
            j = 1
            while j*j <=i:
                memo_list[i] = min(memo_list[i],memo_list[i-j*j]+1)
                j+=1
        return memo_list[n]

#Time Limit Exceeded
import math
class Solution(object):
    def __init__(self):
        self.deepth_list = []
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.minusSquare(n,0)
        return min(self.deepth_list)
        
    def minusSquare(self,n,deepth):
        
        if len(self.deepth_list)!=0:
            if deepth>=min(self.deepth_list):
                return 
        if n==0:
            self.deepth_list.append(deepth)
        deepth+=1
        max_sqrt = int(math.sqrt(n))
        for sqrt in range(max_sqrt,0,-1):
            if n-sqrt**2==0:
                self.deepth_list.append(deepth)
                break
            else:
                self.minusSquare(n-sqrt**2,deepth)