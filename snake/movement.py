# Need to define snake head coordinates
snake_head = [5, 5] # temporary y and x
apple_position = [5,6] # temporary until incorporated
# default position is up
direction = "up"
from Game import GRID


def update_snake_position(direction):
    # Update snake head position
    # snake_head not updating GRID, snake_head needs to be an x and y coordinate pair
    # Does not set previous head to a direction.
    if direction == "left":
        snake_head = [snake_head[0]][snake_head[1] - 1]
    elif direction == "right":
        snake_head = [snake_head[0]][snake_head[1] + 1]
    elif direction == "up":
        snake_head = [snake_head[0] - 1][snake_head[1]]
    elif direction == "down":
        snake_head = [snake_head[0] + 1][snake_head[1]]
    else:
        print("Error: direction is not left, right, up, or down")

    # Removes tail
    if snake_head != apple_position:
        for row in range(len(GRID.grid)):
            for col in range(len(GRID.grid[row])):
                if GRID.grid[row][col] == "left":
                    GRID.grid[row][col - 1] = None
                if GRID.grid[row][col] == "right":
                    GRID.grid[row][col + 1] = None
                if GRID.grid[row][col] == "up":
                    GRID.grid[row - 1][col] = None
                if GRID.grid[row][col] == "down":
                    GRID.grid[row + 1][col] = None
                





