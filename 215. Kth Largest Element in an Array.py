#https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

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


class Solution(object):
    
    def partition_func(self,nums, left, right):

        pivot = nums[left]
        while (left<right):

            while(left < right and nums[right]>=pivot):
                right-=1

            ### nums[right] < pivot
            nums[left]=nums[right]

            while(left < right and nums[left]<=pivot):
                left +=1
            # nums[left]> pivot
            nums[right] = nums[left]

        nums[left] = pivot
        return left 
    

    def recursive_partition(self,nums,left,right,k):

        pivot_index = self.partition_func(nums, left, right)
        if pivot_index==k:
            return nums[k]
        elif pivot_index>k:
            return self.recursive_partition(nums,left,pivot_index-1,k)
        elif pivot_index<k:
            return self.recursive_partition(nums,pivot_index+1,right,k)
        
            
    def findKthLargest(self,nums,k):
        left = 0
        right = len(nums)-1
        k= (len(nums) - 1) -(k-1)
        return self.recursive_partition(nums,left,right,k)


# untime: 116 ms, faster than 22.44% of Python online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.6 MB, less than 17.70% of Python online submissions for Kth Largest Element in an Array.

class Solution(object):
    
    def heapify(self,nums,list_len,parent_index):
        left_index = 2 *parent_index+1
        right_index = left_index+1
        max_index =  parent_index
        if left_index < list_len and nums[left_index] > nums[max_index]:
            max_index = left_index
        if right_index < list_len and nums[right_index] > nums[max_index]:
            max_index = right_index
        if max_index != parent_index:
            nums[parent_index], nums[max_index] = nums[max_index], nums[parent_index]
            self.heapify(nums,list_len,max_index)       
            
    def findKthLargest(self,nums,k):
        list_len = len(nums)
        for n in range(list_len//2-1,-1,-1):
            self.heapify(nums,list_len,n) # initialize to make the parent node always larger than the sub-nodes
        index  =1
        if k == 1:
            return nums[0]
        else:
            for n in range(list_len-1,0,-1): #to rank largest number at the lastest place for each loop by switching
                nums[0],nums[n] = nums[n],nums[0]
                list_len -=1
                self.heapify(nums,list_len,0)
                index+=1
                if index==k:
                    return nums[0]

# Runtime: 56 ms, faster than 56.87% of Python online submissions for Kth Largest Element in an Array.
# Memory Usage: 16 MB, less than 11.37% of Python online submissions for Kth Largest Element in an Array.

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_value = min(nums)
        max_value = max(nums)

        bucket_list = [[] for _ in range(min_value,max_value+1)]
        
        for num in nums:
            bucket_list[num-min_value].append(num)


        sort_list = []

        for bucket in bucket_list[::-1]:
            if len(sort_list)<k:
                sort_list.extend(bucket)
        
        return sort_list[k-1]
