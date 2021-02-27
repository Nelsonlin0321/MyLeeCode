class Solution(object):
    
    def swap_func(self,array,i,j):
        temp = array[i]
        array[i] =array[j]
        array[j] = temp
        
    def partition_func(self,array,start_index,end_index):
        large_than_or_equal_index = start_index
        interval = array[end_index]
        for loop_index in range(start_index,end_index+1):
            loop_num = array[loop_index]
            if loop_num >= interval:## descending
                self.swap_func(array,loop_index,large_than_or_equal_index)
                large_than_or_equal_index +=1
        return large_than_or_equal_index-1

    def recursive_partition_func(self,array,k,start_index,end_index):
        if end_index-start_index>=1:
            interval_index =self.partition_func(array,start_index,end_index)
            if interval_index==k:
                return array[k]
            elif k<interval_index:
                return self.recursive_partition_func(array,k,start_index,interval_index-1)
            elif k>interval_index:
                return self.recursive_partition_func(array,k,interval_index+1,end_index)
        else:
            return array[k]
                
            
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = k-1
        start_index,end_index = 0,len(nums)-1
        KthLargest =self.recursive_partition_func(nums,k,start_index,end_index)
        
        return KthLargest

nums = [3,2,1,5,6,4]
k = 2
KthLargest = solution.findKthLargest(nums, k)