from enum import Enum

class Direction(Enum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3

class Snake:
    #requires a starting position because a snake needs to know the locations of it's segments
    
    def __init__(self, starting_position):
        self.direction = Direction.UP
        #first index will point to the head, last one is the lil tail
        self.segments = [starting_position]
        self.segments = [self.get_new_head()] + self.segments

    def get_new_head(self):
        new_head = self.segments[0]
        if self.direction == Direction.UP:
            new_head[0] = (new_head[0] -  1) % 31
        elif self.direction == Direction.RIGHT:
            new_head[1] = (new_head[1]) + 1 % 31
        elif self.direction == Direction.DOWN:
            new_head[0] = (new_head[0]) + 1 % 31
        elif self.direction == Direction.LEFT:
            new_head[1] = (new_head[1]) - 1 % 31
        return new_head
    
    #moves the snake
    def update(self):
        self.segments = [self.get_new_head()] + self.segments
        self.segments.pop()
    
    #grows the snake, same as moving except keeps the tail
    def grow(self):
        self.segments = [self.get_new_head()] + self.segments

    def intersects(self, position):
        return position in self.segments
