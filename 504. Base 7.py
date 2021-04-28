#https://leetcode.com/problems/base-7/submissions/
#Runtime: 20 ms, faster than 43.59% of Python online submissions for Base 7.
#Memory Usage: 13.4 MB, less than 70.09% of Python online submissions for Base 7.

class Solution(object):
    def convertToBase7(self,num):
        """
        :type num: int
        :rtype: str
        """
        isneg = num<0
        if isneg:
            num = -num
        
        sig_digit = num - num//7 *7
        num = num-sig_digit
        max_digit = 0
        for n in range(8,0,-1):
            if  7**n <=num:
                max_digit = n
                break
        digit_list = []
        for digit_pos in range(max_digit,0,-1):
            digit = num // (7**digit_pos)
            base = digit*(7**digit_pos)
            digit_list.append(str(digit))
            num = num - base

        digit_list.append(str(sig_digit ))

        if isneg:
            return '-'+''.join(digit_list)
        else:
            return ''.join(digit_list)