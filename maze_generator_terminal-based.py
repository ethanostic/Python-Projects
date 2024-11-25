#region Generate maze size

# Imports and pre-defined variables
import json
y_dict = {}
maze_dict = {}

# Odd number input greater than or equal to 5 for x
while True:
    x_length = int(input("X: "))
    if x_length >= 5:
        if x_length % 2 != 0:
            break
x_list = list(range(1, x_length + 1))

# Odd number input greater than or equal to 5 for y
while True:
    y_length = int(input("Y: "))
    if y_length >= 5:
        if y_length % 2 != 0:
            break
y_list = list(range(1, y_length + 1))
for number in y_list:
    y_dict[number] = "path"
    

# generate maze
for number in x_list:
    maze_dict[number] = y_dict.copy()

#endregion

#region Set standard maze walls

# Set unknowns
for x_key, y_dict in maze_dict.items():
    for y_key in y_dict:
        if x_key % 2 != 0:
            if y_key % 2 == 0:
                maze_dict[x_key][y_key] = "unknown"
    for y_key in y_dict:
        if x_key % 2 == 0:
            if y_key % 2 != 0:
                maze_dict[x_key][y_key] = "unknown"

# Sets borders
for x_key, y_dict in maze_dict.items():
    for y_key in y_dict:
        if x_key == 1 or x_key == x_length:
            maze_dict[x_key][y_key] = "wall"
        elif y_key == 1 or y_key == y_length:
            maze_dict[x_key][y_key] = "wall"

# Sets pillars
for x_key, y_dict in maze_dict.items():
    for y_key in y_dict:
        if x_key % 2 != 0:
            if y_key % 2 != 0:
                maze_dict[x_key][y_key] = "wall"

#endregion

# fill in maze

print(json.dumps(maze_dict, indent=4))

current_cell_x = 2
current_cell_y = 2

# information from up, down, left, and right based on current cell

