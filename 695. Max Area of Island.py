#https://leetcode.com/problems/max-area-of-island/submissions/
# Runtime: 152 ms, faster than 36.95% of Python3 online submissions for Max Area of Island.
# Memory Usage: 16.6 MB, less than 52.21% of Python3 online submissions for Max Area of Island.

class Solution:

    def maxAreaOfIsland(self, grid) -> int:
        island_area_list =[]
        has_island = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]==1:
                    has_island = True
                    area_size = 0
                    area_size = self.get_area_size(grid,area_size,x,y)
                    island_area_list.append(area_size)
        if not has_island:
            return 0
        return max(island_area_list)
                    
                        
    def inside_box(self,grid,x,y):
        y_n = len(grid )
        x_n = len(grid[0])
        return (0<=x<=x_n-1) and ((0<=y<=y_n-1)) and grid[y][x]!=2

    def get_area_size(self,grid,area_size,x,y):
        area_size +=1
        grid[y][x] =2
        x_right,y_right = x+1,y
        if self.inside_box(grid,x_right,y_right):
            if grid[y_right][x_right] ==1:
                area_size = self.get_area_size(grid,area_size,x_right,y_right)

        # up
        x_up,y_up = x,y+1
        if self.inside_box(grid,x_up,y_up):
            if grid[y_up][x_up] ==1:
                area_size = self.get_area_size(grid,area_size,x_up,y_up)

        # left
        x_left,y_left = x-1,y
        if self.inside_box(grid,x_left,y_left):
            if grid[y_left][x_left] ==1:
                area_size = self.get_area_size(grid,area_size,x_left,y_left)

        # down
        x_down,y_down = x,y-1
        if self.inside_box(grid,x_down,y_down):
            if grid[y_down][x_down] ==1:
                area_size = self.get_area_size(grid,area_size,x_down,y_down)
        
        return area_size

#Runtime: 128 ms, faster than 90.35% of Python3 online submissions for Max Area of Island.
#Memory Usage: 16.2 MB, less than 60.61% of Python3 online submissions for Max Area of Island.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col]*row
        maxArea = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, self.dfs(r, c, grid))
        
        return maxArea
    
    def dfs(self, r, c, grid):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
            return 0
        if not grid[r][c]:
            return 0
        grid[r][c] = 0
        return 1 + self.dfs(r+1, c, grid) + self.dfs(r-1, c, grid) + self.dfs(r, c+1, grid) + self.dfs(r, c-1, grid) # 递推公式


            
            
    
            