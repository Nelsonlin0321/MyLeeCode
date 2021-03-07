import numpy as np

nums = list(np.random.randint(0, 3, 20))

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        boundary_dict = self.boundary_dict_func(nums)
        color = 0
        start = 0
        end = boundary_dict[0]
        self.number_replace(nums,boundary_dict,start,end,color)
        
        color = 1
        start = boundary_dict[0]
        end = boundary_dict[1]
        self.number_replace(nums,boundary_dict,start,end,color)
        
    def boundary_dict_func(self,nums):
        counter = {0: 0,
                   1: 0,
                   2: 0}

        for num in nums:
            counter[num] += 1

        counter[1] = counter[1] + counter[0]

        counter[2] = counter[1] + counter[2]

        return counter

    def number_replace(self,nums,boundary_dict,start,end,color):
        inplaced_count = 0
        for replace_index in range(start,end):
            if inplaced_count + 1 > boundary_dict[color]:
                break
            if nums[replace_index] == 0:
                inplaced_count += 1
            else:
                for look_index in range(replace_index + 1, len(nums)):
                    if nums[look_index] == color:
                        nums[replace_index], nums[look_index] = nums[look_index], nums[replace_index]
                        inplaced_count += 1
                        break


solution = Solution()

solution.sortColors(nums)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, curr, j = 0, 0 , len(nums) - 1
        while curr <= j:
            if nums[curr] == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                j -= 1
            elif nums[curr] == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1
                curr += 1
            else:
                curr += 1

solution = Solution()
solution.sortColors(nums)