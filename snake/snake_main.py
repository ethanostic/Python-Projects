#I added some comments mixed in with yours as a response, I hope it's clear what i mean

# This is general outline for the snake game. feel free to modify it or add to it with comments or real code. I'll get to it later tomorrow.

# Creates a grid that represents the area the snake can travel, we can have a "game" object that does this the moment it's created
    # snake cells are mark with a direction to show how the snake needs to move, Can this be done in a snake class, by giving a snake a direction property, like an enum? I created an example snake class to hopefully explain what i mean. 
    # a snake cell that is not pointing toward anything is the tail end of the snake and therefore should be removed in the next frame
# Check the grid every set period of time (snake speed) to change snake position
    # if a cell that the snakes travels to is occupied by its body or a wall, then game over.
# Connect this grid to pygame
# Bind arrow keys or WASD to change the direction of the snake.
# Randomly generate the food source after the food source has been eaten.
    # generate the food source not in the snake body.

#imports
import pygame
from Game import Game

#constants, because maybe it's a good idea to know how big we want our squares to be in pixels
GRID_SIZE   = 31
CELL_IN_PX  = 16

pygame.init()
#calculate the size of our window, based on the size of cells in pixels
window_width = GRID_SIZE * CELL_IN_PX
window_height= GRID_SIZE * CELL_IN_PX
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

# Creates a 31x31 grid
#grid = create_grid()
game = Game(31)
game.start()

# snake main loop
while running:
    #pass the events to our game so that we can handle them correctly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #this should handle all the update logic, like placing apples and updating the snake
    game.update()
    
    #this should do only display things, like actually drawing the snake and the apple
    game.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


