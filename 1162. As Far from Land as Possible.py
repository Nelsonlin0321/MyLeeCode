# Runtime: 656 ms, faster than 46.78% of Python3 online submissions for As Far from Land as Possible.
# Memory Usage: 15.5 MB, less than 41.49% of Python3 online submissions for As Far from Land as Possible.

class Solution:
    def maxDistance(self, grid) -> int:
        queque_list = [] # 队列
        n = len(grid)
        for x in range(n):
            for y in range(n):
                if grid[x][y] ==1:
                    #  添加岛屿到队列
                    queque_list.append((x,y))
        
        distance = -1
        
        # 没有岛屿返回-1 / #没有水的话 返回-1
        if len(queque_list)==0 or len(queque_list)==n*n :
            return distance
          

        while (len(queque_list)!=0):

            distance +=1
            #遍历当前元素
            # 必须使用索引，因为后面会继续往后添加有数
            size = len(queque_list) # 获取当前层级的元素个数
            
            for index in range(size): # 遍历这个层级的元素
                x,y = queque_list[index]
                
                left_x,left_y = x-1,y
                if self.inArea(grid,left_x,left_y):
                    queque_list.append((left_x,left_y))
                    # 标记已经访问的位置，避免重复访问
                    grid[left_x][left_y] = 2
                    
                right_x,right_y = x+1,y
                if self.inArea(grid,right_x,right_y):
                    queque_list.append((right_x,right_y))
                    grid[right_x][right_y] = 2
                    
                up_x,up_y = x,y+1
                if self.inArea(grid,up_x,up_y):
                    queque_list.append((up_x,up_y))
                    grid[up_x][up_y] = 2
                    
                down_x,down_y = x,y-1
                if self.inArea(grid,down_x,down_y ):
                    queque_list.append((down_x,down_y))
                    grid[down_x][down_y] = 2            
                    
                
            # 弹出这一层级的元素
            queque_list = queque_list[size:]

        return distance

    def inArea(self,grid,x,y):
        n  = len(grid)
        return (0<=x<=n-1) and (0<=y<=n-1) and grid[x][y]==0
    
