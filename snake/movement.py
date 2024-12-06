# functions called by arrow keys
# this is a rough idea. Its not incorporated well with the rest of the code.

# Need to define snake head coordinates
snake_head = [5, 5] # temporary y and x
apple_position = [5,6] # temporary

def move_left():
    eaten = False
    # Head appears x - 1 based on previous head position
    snake_head = [snake_head[0]][snake_head[1] - 1]
    if snake_head == apple_position:
        eaten = True
    drop_tail(eaten)

def move_right():
    eaten = False
    # x + 1
    snake_head = [snake_head[0]][snake_head[1] + 1]
    if snake_head == apple_position:
        eaten = True
    drop_tail(eaten)

def move_up():
    eaten = False
    # y - 1
    snake_head = [snake_head[0] - 1][snake_head[1]]
    if snake_head == apple_position:
        eaten = True
    drop_tail(eaten)

def move_down():
    eaten = False
    # y + 1
    snake_head = [snake_head[0] + 1][snake_head[1]]
    if snake_head == apple_position:
        eaten = True
    drop_tail(eaten)


# this is assuming the grid starts in the top left corner
# ex. x,y

# 1,1  2,1  3,1
# 1,2  2,2  3,2
# 1,3  2,3  3,3

# drops snake tale unless the head has com upon an apple

# Assume that segments are noted in the main grid

from Game import Game

def drop_tail(eaten):
    if eaten == False:
        for row in range(grid_size):
            for col in range(grid_size):
                #if nothing is pointing toward the snake segment, then it is a tail and should be removed.