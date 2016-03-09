################################
# Author: Asher Minden-Webb    #
# Date: February 8, 2016       #
################################

def is_path(grid):
    """    
    Returns true if there is a path from grid[0][0] to a cell containing 2.
    
    Cells containing 1 are paths and cells containing 0 are walls.  Paths 
    may only move vertically and horizontally, not diagonally.
    
    @param grid: nxm 2-dimensional list representing a maze
    @rtype: boolean
    
    """
    if len(grid) == 0 or len(grid[0]) == 0:
        return False
    # Call to recursive helper function, made with *copy* of grid
    return _is_path(grid[:], 0, 0)

def _is_path(grid, x, y):
    """
    Helper function for is_path().  "grid" parameter will be modified.
    
    @param grid: nxm 2-dimensional list, modifiable
    @param x: x-coordinate to search
    @param y: y-coordinate to search
    @rtype boolean
    
    """
    # Recursive breadth-first search, from top-left to bottom-right of grid.
    # Visited cells are marked with -1
    if grid[y][x] == 2:
        grid[y][x] = -1
        return True
    if grid[y][x] in [0, -1]:
        grid[y][x] = -1
        return False
    return \
        (_is_path(grid, x, y + 1) if len(grid) > y + 1 else False) or \
        (_is_path(grid, x + 1, y) if len(grid[0]) > x + 1 else False)
        