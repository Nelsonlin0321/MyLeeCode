import numpy as np

var_list = np.random.randint(0,100,20)

class Solution(object):
    def bubble_sort(self,numbers):
        """
        :type numbers: List[int]
        """
        for end_index in list(range(len(numbers)))[::-1]:
            for index in range(end_index):
                first_number = numbers[index]
                second_number = numbers[index+1]
                if second_number < first_number:
                    numbers[index] = second_number
                    numbers[index+1] = first_number

solution = Solution()
solution.bubble_sort(var_list)