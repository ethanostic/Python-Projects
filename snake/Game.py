from random import randrange
from Snake import Snake
from Apple import Apple
#import pygame

class Game:
    #the constructor
    def __init__(self, grid_size):
        #for drawing the grid
        self.grid = [[None]* grid_size for i in range(grid_size)]
        
    #responsible for creating a snake
    def start(self):
        half_of_grid = len(self.grid)//2
        self.snake = Snake([half_of_grid, half_of_grid ])
        self.add_new_apple()

    #can be called to magically spawn an apple, should probably eat the old apple
    def add_new_apple(self):
        # spawns apple at random position
        def spawn_apple():
            self.apple_position = [randrange(len(self.grid)), randrange(len(self.grid))]
        spawn_apple()
        while self.snake.intersects(self.apple_position):
            spawn_apple()
        self.apple = Apple(self.apple_position)

    #updates the snake, and the apple, this should likely update the direction for the snake
    def update(self):
        if self.snake.intersects(self.apple.position):
            self.add_new_apple()
            self.snake.grow()
        else:
            #maybe update needs a direction argument, cause it does the move?
            self.snake.update()
    
    #this has access to exactly what to draw and where
    def draw(self, screen):
        for row_idx, row in enumerate(self.grid):
            for col_idx, col in enumerate(row):
                if [row_idx, col_idx] in self.snake.segments:
                    print('#',end="")
                elif [row_idx, col_idx] == self.apple.position:
                    print('O',end="")
                else:
                    print(' ',end="")
            print("")
    
    #takes one position
    def draw_apple(self, position):
        print("I am drawing apple")

# Creates the grid as one instance
GRID = Game(3)

    #def draw(self, screen):
    #    #draws grid
    #    self.draw()

