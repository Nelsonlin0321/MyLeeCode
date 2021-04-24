# https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/
# Runtime: 116 ms, faster than 12.09% of Python online submissions for Different Ways to Add Parentheses.
# Memory Usage: 20.8 MB, less than 10.44% of Python online submissions for Different Ways to Add Parentheses.
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        import re
        expression_split= re.split('([^0-9])',expression)
        if len(expression_split)==1:
            return expression_split
        self.combination_list = []
        self.recursive_add_paren(expression_split)
        return [eval(way) for way in set(self.combination_list)]

    def recursive_add_paren(self,expression_split):
        if len(expression_split)==3:
            self.combination_list.append("".join(expression_split))
        else:
            for index in range(int((len(expression_split)-1)/2)):
                paren_item= expression_split[index*2:index*2+3]
                paren_item = "("+"".join(paren_item)+")"
                sub_expression_split = expression_split[:index*2]+[paren_item]+expression_split[index*2+3:]
                self.recursive_add_paren(sub_expression_split)
                
#Runtime: 20 ms, faster than 88.55% of Python online submissions for Different Ways to Add Parentheses.
#Memory Usage: 13.6 MB, less than 83.13% of Python online submissions for Different Ways to Add Parentheses.                
class Solution(object):
    
    def helper(self,oper,j,k):
        if oper=='+':
            return j+k
        elif oper =='-':
            return j-k
        else:
            return j*k
        
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        
        if expression.isdigit():
            return [int(expression)]
        res = []
        
        for i in range(len(expression)):
            if expression[i] in "+-*":
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(expression[i],j,k))
        return res 
        
