# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

# Runtime: 56 ms, faster than 24.12% of Python online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 13.8 MB, less than 28.66% of Python online submissions for Two Sum II - Input array is sorted.

class Solution(object):
    def twoSum(self,numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pass_number = None
        for (i,number_one) in enumerate(numbers[:-1]):
            if number_one==pass_number:
                continue
            else:
                for(j,number_two) in enumerate(numbers[i+1:]):
                    if number_two+number_one ==target:
                        return [i+1,j+i+2]
                    elif number_one==number_two:
                        pass_number = number_one

# Runtime: 64 ms, faster than 17.19% of Python online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 13.7 MB, less than 48.97% of Python online submissions for Two Sum II - Input array is sorted.

class Solution(object):
    
    def drop_duplicate(self,numbers):
        unique_numbers=[]
        for num in numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        return unique_numbers
        
    def find_number(self,numbers, target):
        for start_index in range(len(numbers)):
            start_number = numbers[start_index]
            if start_number<=target:
                for end_index in range(len(numbers)):
                    end_index = len(numbers)-1 - end_index
                    end_number = numbers[end_index]
                    if start_number+end_number==target:
                        return [start_number,end_number]
                    
    def twoSum(self, numbers, target):

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        unique_numbers = self.drop_duplicate(numbers)
        
        two_numbers = self.find_number(unique_numbers, target)
        
        index_list =[]
        
        for (index,num) in enumerate(numbers):
            if len(two_numbers)!=0:
                if num in two_numbers:
                    two_numbers.remove(num)
                    index_list.append(index+1)
                    
        return index_list
        