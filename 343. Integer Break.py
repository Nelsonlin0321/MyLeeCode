#https://leetcode.com/problems/integer-break/submissions/
# Runtime: 24 ms, faster than 94.91% of Python3 online submissions for Integer Break.
# Memory Usage: 14.3 MB, less than 15.68% of Python3 online submissions for Integer Break.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n==1:
            return n
        
        max_value = n-1
        for divisor in range(2,n//2+1):
            divided = n//divisor

            remain = n-(divided*divisor)
            if remain ==0:    
                if max_value < divided**divisor:
                    max_value = divided**divisor
            else:
                value_1 = (divided**(divisor-1))*(divided+remain)
                divided+=1
                remain = n-(divided*divisor)
                value_2 = (divided**(divisor-1))*(divided+remain)
                value = value_1 if value_1 > value_2 else value_2 
                if max_value < value:
                    max_value = value
        return max_value
