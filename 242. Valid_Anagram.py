# https://leetcode.com/problems/valid-anagram/submissions/
#Runtime: 40 ms, faster than 75.64% of Python online submissions for Valid Anagram.
#Memory Usage: 18.1 MB, less than 5.02% of Python online submissions for Valid Anagram.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_dict ={}
        t_dict ={}
        for (s_char,t_char) in zip(s,t):
            if s_char in s_dict:
                s_dict[s_char]+=1
            else:
                s_dict[s_char]=1

            if t_char in t_dict:
                t_dict[t_char]+=1
            else:
                t_dict[t_char]=1

        return s_dict==t_dict