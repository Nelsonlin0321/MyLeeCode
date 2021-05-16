# https://leetcode.com/problems/making-a-large-island/submissions/
# Runtime: 3340 ms, faster than 74.54% of Python3 online submissions for Making A Large Island.
# Memory Usage: 23.8 MB, less than 72.51% of Python3 online submissions for Making A Large Island.
from copy import deepcopy
class Solution:
    
    def inArea(self,x,y,grid): # 判断是否为有效区域的陆地
        width = len(grid)
        heigth = len(grid[0])
    
        return 0<=x<width and 0<=y<heigth

    def get_grid(self,x,y,grid,island_grid): # 返回该岛的所有方格

        if self.inArea(x,y,grid) and grid[x][y]==1:
            grid[x][y] = -1 # 访问过多的陆地标记为 -1

            island_grid.append((x,y))
            island_grid = self.get_grid(x+1,y,grid,island_grid)
            island_grid = self.get_grid(x-1,y,grid,island_grid)
            island_grid = self.get_grid(x,y+1,grid,island_grid)
            island_grid = self.get_grid(x,y-1,grid,island_grid)

        return island_grid
    
    def largestIsland(self, grid):
        
        grid_id = deepcopy(grid)# 用于记录岛屿方格属于哪一个岛屿
        island_id = 0 # 记录岛屿的unique id
        has_island = False
        max_island = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1: #访问到陆地
                    # 计算这个陆地的方格
                    has_island = True
                    island_grid = []
                    island_grid = self.get_grid(x,y,grid,island_grid)
                    island_area = len(island_grid)
                    max_island =island_area if island_area>max_island else  max_island
                    for (i,j) in island_grid:
                        grid[i][j] = island_area
                        grid_id[i][j] = island_id #将所有的岛屿的方格都标记上该岛屿的标签
                    island_id+=1 # 更新岛屿 unique id
                    
        if not has_island:
            return 1

        has_water = False
        #遍历每一个水域形成的陆地大小
        area_size = max_island
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==0: #访问到水域    
                    has_water = True
                    # 判断是这个块水域是否可以连接其他陆地
                    connect_islands={}
                    for (x_,y_) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                        if self.inArea(x_,y_,grid) and grid[x_][y_]!=0: # ！=0 说明就是之前访问过的陆地
                            #  island_size
                            island_size = grid[x_][y_]
                            island_id = grid_id[x_][y_]
                            connect_islands[island_id] = island_size
                                            
                    
                    area_size = max(sum(connect_islands.values())+1,area_size)
        
        if not has_water:
            return max_island
        
        return area_size 
