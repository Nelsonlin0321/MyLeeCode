#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/submissions/
#Runtime: 4600 ms, faster than 5.01% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
#Memory Usage: 30.6 MB, less than 5.47% of Python online submissions for Kth Smallest Element in a Sorted Matrix

class Solution(object):
    
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import numpy as np
        for i in range(k):
            row_num = [ col[0]  for col in matrix if len(col)>0]
            matrix = [ col for col in matrix if len(col)>0]
            min_index = np.argmin(row_num)
            i_smallest = row_num[min_index]
            matrix[min_index].remove(i_smallest)
        return i_smallest