# This is general outline for the snake game. feel free to modify it or add to it with comments or real code. I'll get to it later tomorrow.

# Creates a grid that represents the area the snake can travel
    # snake cells are mark with a direction to show how the snake needs to move
    # a snake cell that is not pointing toward anything is the tail end of the snake and therefore should be removed in the next frame
# Check the grid every set period of time (snake speed) to change snake position
    # if a cell that the snakes travels to is occupied by its body or a wall, then game over.
# Connect this grid to pygame
# Bind arrow keys or WASD to change the direction of the snake.
# Randomly generate the food source after the food source has been eaten.
    # generate the food source not in the snake body.