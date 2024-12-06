from enum import Enum

class Direction(Enum):
    UP = 0,
    RIGHT = 1,
    DOWN = 2,
    LEFT = 3

class Snake:
    #requires a starting position because a snake needs to know the locations of it's segments
    
    def __init__(self, x, y):
        self.direction = Direction.UP
        self.segments = []

    def update(self):
        pass
    
    def draw(self, screen):
        pass

    def intersects(self, position):
        return position in self.segments
