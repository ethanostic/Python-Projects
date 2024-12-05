def create_grid():
    """Returns an empty 31x31 grid for the game"""
    maze_dimensions = 31

    grid = {}
    for y in range(1, maze_dimensions + 1):
        grid[y] = {}
        for x in range(1, maze_dimensions + 1):
            grid[y][x] = None

    return grid