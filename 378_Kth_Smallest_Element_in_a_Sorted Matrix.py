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


#Runtime: 212 ms, faster than 51.72% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
#Memory Usage: 19.1 MB, less than 75.64% of Python online submissions for Kth Smallest Element in a Sorted Matrix.   
    
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = [(row[0],i,0) for (i,row) in enumerate(matrix )]
        heapq.heapify(heap)
        value = 0
        for _ in range(k): # pop k times to get k_smalltest
            value,row_i,col_j = heapq.heappop(heap)# pop the samllest value with row_i, col_j
            if col_j+1<len(matrix[0]) : # only 0,1,2 < 3 for one row only pop the len(row) times
                heapq.heappush(heap,(matrix[row_i][col_j+1],row_i,col_j+1))
        return value

#Runtime: 136 ms, faster than 91.78% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
#Memory Usage: 19 MB, less than 92.53% of Python online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from bisect import bisect
        lo, hi  = matrix[0][0],matrix[-1][-1]
        
        while (lo<hi):
            mid = lo + (hi-lo)//2
            mid_count = sum([bisect(row,mid) for row in matrix]) # the number of element smaller or equal to middle value
            if mid_count<k: # <=mid is smaller than k
                lo = mid + 1 
                # tricky
                # make lo can equal to hi , if lo = 13, and hi = 14, mid = 13 ,which will be a dead loop. but if lo=12 and hi = 14 , mid = 13, mid is the number of matrix, so add to add one to eqaul to hi.
            else:
                hi  =mid
        return lo
                
            
