#https://leetcode.com/problems/delete-operation-for-two-strings/submissions/
#Runtime: 620 ms, faster than 6.48% of Python3 online submissions for Delete Operation for Two Strings.
#Memory Usage: 17.9 MB, less than 33.36% of Python3 online submissions for Delete Operation for Two Strings.

# bottom up
class Solution:
    def __init__(self):
        self.dp = None

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [ [None for _ in  range(len(word2)+1)] 
              for _ in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                self.dp[i][j] = self.__minDistance(word1[:i],word2[:j])
        
        return self.dp[len(word1)][len(word2)]
                    

    def __minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))
        
        elif word1==word2:
            return 0
        
        if word1[-1]!=word2[-1]:
            return 1+min(self.dp[len(word1)-1][len(word2)],self.dp[len(word1)][len(word2)-1])
        else:
            return self.dp[len(word1)-1][len(word2)-1]

# up to down
#Runtime: 568 ms, faster than 7.60% of Python3 online submissions for Delete Operation for Two Strings.
#Memory Usage: 17.2 MB, less than 43.37% of Python3 online submissions for Delete Operation for Two Strings.
class Solution:
    def __init__(self):
        self.dp = None

    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [ [None for _ in  range(len(word2)+1)] 
              for _ in range(len(word1)+1)]
        
        return self.__minDistance(word1,word2)
                    

    def __minDistance(self, word1: str, word2: str) -> int:

        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))

        elif word1==word2:
            return 0

        if word1[-1]!=word2[-1]:
            if self.dp[len(word1)-1][len(word2)] is None:
                self.dp[len(word1)-1][len(word2)] = self.__minDistance(word1[:-1],word2)
            if self.dp[len(word1)][len(word2)-1] is None:
                self.dp[len(word1)][len(word2)-1] = self.__minDistance(word1,word2[:-1])
            self.dp[len(word1)][len(word2)] = 1+min(self.dp[len(word1)-1][len(word2)],self.dp[len(word1)][len(word2)-1] ) 
            return self.dp[len(word1)][len(word2)]
        else:
            if self.dp[len(word1)-1][len(word2)-1] is None:
                self.dp[len(word1)-1][len(word2)-1] = self.__minDistance(word1[:-1],word2[:-1])            
            return self.dp[len(word1)-1][len(word2)-1]
        