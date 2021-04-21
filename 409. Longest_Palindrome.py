#https://leetcode.com/problems/longest-palindrome/submissions/
#Runtime: 20 ms, faster than 81.61% of Python online submissions for Longest Palindrome.
#Memory Usage: 13.4 MB, less than 89.37% of Python online submissions for Longest Palindrome.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char]=1
            else:
                char_dict[char]+=1
        sum_count = 0
        add_one_flag = False
        for char in char_dict:
            division = char_dict[char]/2
            count = int(division)
            sum_count +=count
            if count*2<char_dict[char]:
                add_one_flag=True

        if add_one_flag:
            sum_count = sum_count*2+1
        else:
            sum_count = sum_count*2
        return sum_count

# the best solution
#Runtime: 16 ms, faster than 95.11% of Python online submissions for Longest Palindrome.
#Memory Usage: 13.6 MB, less than 38.22% of Python online submissions for Longest Palindrome.
class Solution:
    def longestPalindrome(self, s):
        dic={}
        for i in s:
            if i in dic:
                del dic[i]
            else:
                dic[i]=1
        if not dic :
            return len(s)
        return len(s)-len(dic)+1