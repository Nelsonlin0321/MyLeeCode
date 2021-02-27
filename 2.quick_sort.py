import numpy as np
import random

array = list(np.random.randint(0,100,10))

class Solution(object):
    
    def swap_func(self,array,i,j):
        temp = array[i]
        array[i] =array[j]
        array[j] = temp
        
    def partition_func(self,array,start_index,end_index):
        less_than_or_equal_index = start_index
        interval = array[end_index]
        for loop_index in range(start_index,end_index+1):
            loop_num = array[loop_index]
            if loop_num <= interval:
                self.swap_func(array,loop_index,less_than_or_equal_index)
                less_than_or_equal_index +=1
        return less_than_or_equal_index-1
    ### the boundary, in which the numbers are less or equal to pivot, at the begining , it should be minus one
    # because we know only after comparing 
    def recursive_partition_func(self,array,start_index,end_index):
        if end_index-start_index>1:
            interval_index =self.partition_func(array,start_index,end_index)
            self.recursive_partition_func(array,start_index,interval_index-1)
            self.recursive_partition_func(array,interval_index+1,end_index)
    def quick_sort(self,numbers):
        """
        :type numbers: List[int]
        """
        start_index = 0
        end_index = len(numbers)-1
        self.recursive_partition_func(numbers,start_index,end_index)

solution = Solution()
solution.quick_sort(array)
