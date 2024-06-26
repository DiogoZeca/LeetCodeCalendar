# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland.
# These rectangular areas are called groups. 
# No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1).
# Find the coordinates of the top left and bottom right corner of each group of farmland. 
# A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. 
# If there are no groups of farmland, return an empty array. You may return the answer in any order.



class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(land), len(land[0])
        
        def findFarmlandCoordinates(row, col):
            coordinates = [row, col]
            r, c = row, col
            
            while r < m and land[r][col] == 1:
                r += 1
            while c < n and land[row][c] == 1:
                c += 1
            
            coordinates.extend([r - 1, c - 1])
            
            for i in range(row, r):
                for j in range(col, c):
                    land[i][j] = 0
            
            return coordinates
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    result.append(findFarmlandCoordinates(i, j))
        
        return result
