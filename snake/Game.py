from random import randrange
from snake.Snake import Snake
from Apple import Apple

class Game:
    #the constructor
    def __init__(self, grid_size):
        self.grid = [[0]* grid_size for i in range(grid_size)]
     
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
        #maybe update needs a direction argument?
        self.snake.update()
        if self.snake.intersects(self.apple.position):
            self.add_new_apple()
            # and somehow increase snake length
    
    #this could draw the empty grid
    def draw_background(self):
        print("I am drawing the background")

    #takes a list of positions
    def draw_snake(self, segments):
        print("i am drawing a snake")
    
    #takes one position
    def draw_apple(self, position):
        print("I am drawing apple")

    def draw(self, screen):
        #draws grid
        self.draw_background()
        #draws snake overtop as green cell
        self.draw_snake(self.snake.segments)
        #draws apple as red cell
        self.draw_apple(self.apple.position)

