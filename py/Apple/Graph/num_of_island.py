# number of islands
# Example 1
# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Example 2
# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3





def numIslands(grid):
    # empty input
    if not grid:
        return 0
    
    row, col = len(grid), len(grid[0])
    # aux function : delete the whole island
    def aux_delete_island(x,y):
        # check board
        if 0<=x and x<row and 0<=y and y<col:
            if grid[x][y] == "1":
                grid[x][y] = 0
                aux_delete_island(x+1,y)
                aux_delete_island(x-1,y)
                aux_delete_island(x,y+1)
                aux_delete_island(x,y-1)
        # else pass do nothing

    res = 0 
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                res += 1
                aux_delete_island(i,j)
    return res