import numpy as np
import random

nums_list = list(np.random.randint(0,100,10))

class Solution(object):
    
    def heapify(self,num_list,list_len,parent_index):
        left_index = 2 *parent_index+1
        right_index = left_index+1
        max_index =  parent_index
        if left_index < list_len and num_list[left_index] > num_list[max_index]:
            max_index = left_index
        if right_index < list_len and num_list[right_index] > num_list[max_index]:
            max_index = right_index
        if max_index != parent_index:
            num_list[parent_index], num_list[max_index] = num_list[max_index], num_list[parent_index]
            heapify(num_list,list_len,max_index)
                
            
    def heap_sort(self,num_list):
        list_len = len(num_list)
        for n in range(list_len//2-1,-1,-1):
            self.heapify(num_list,list_len,n) # initialize to make the parent node always larger than the sub-nodes
        for n in range(list_len-1,0,-1): #to rank largest number at the lastest place for each loop by switching
            num_list[0],num_list[n] = num_list[n],num_list[0]
            #  further to take the next largest number
            list_len -=1
            self.heapify(num_list,list_len,0)
        return num_list

solution = Solution()
solution.heap_sort(num_list)