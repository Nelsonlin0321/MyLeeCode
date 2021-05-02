#https://leetcode.com/problems/edit-distance/submissions/
#Runtime: 96 ms, faster than 96.06% of Python online submissions for Edit Distance.
#Memory Usage: 17.3 MB, less than 11.67% of Python online submissions for Edit Distance.

from copy import copy
class Solution(object):
    def __init__(self):
        self.edit_metrics = None
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word2_array = [ None for _ in range(len(word2)+1)] 
        self.edit_metrics = [copy(word2_array) for _ in range(len(word1)+1)] 
        return self.__minDistance(word1, word2)
    
    def __minDistance(self,word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==0:
            self.edit_metrics[0][len(word2)] = len(word2)
            return self.edit_metrics[0][len(word2)]
        elif len(word2)==0:
            self.edit_metrics[len(word1)][0] = len(word1)
            return self.edit_metrics[len(word1)][0]


        if word1[-1] == word2[-1]: # equal
            if self.edit_metrics[len(word1)][len(word2)] is None:
                self.edit_metrics[len(word1)][len(word2)] = self.__minDistance(word1[:-1],word2[:-1])
                return self.edit_metrics[len(word1)][len(word2)]
            else:
                return self.edit_metrics[len(word1)][len(word2)]
        else:
            if self.edit_metrics[len(word1)-1][len(word2)-1] is None: # replace one of the
                self.edit_metrics[len(word1)-1][len(word2)-1]  = self.__minDistance(word1[:-1],word2[:-1])

            if self.edit_metrics[len(word1)-1][len(word2)] is None: # remove  the last char from word 1
                self.edit_metrics[len(word1)-1][len(word2)] = self.__minDistance(word1[:-1],word2)

            if self.edit_metrics[len(word1)][len(word2)-1] is None:# remove  the last char from word 2
                self.edit_metrics[len(word1)][len(word2)-1] = self.__minDistance(word1,word2[:-1])

            return 1+ min(
                [self.edit_metrics[len(word1)-1][len(word2)-1],# replace
                 self.edit_metrics[len(word1)-1][len(word2)] ,# remove from word1
                 self.edit_metrics[len(word1)][len(word2)-1]  ## remove from word2
                ]
            )