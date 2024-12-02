import json
import random
x_dict = {}
y_dict = {}

# Make the X dictionary
x_length = int(input("X: "))
for i in range(1, x_length+1):
    x_dict[i] = None

# Make the Y dictionary and assign the height and rain and nest it in the X dictionary.
y_length =  int(input("Y: "))
for y in x_dict.keys():
    for i in range(1, y_length+1):
        y_dict[i] = height_and_rain = [i + random.randint(0, 1), 1]
    x_dict[y] = y_dict.copy()

def erosion():
    for x_key, y_dict in x_dict.items():
        for y_key, current_cell_data in y_dict.items():
    
            Middle = current_cell_data
            Middle_height = Middle[0]
            Middle_rain = Middle[1]
            Total_height_Middle = sum(Middle)

            North = x_dict.get(x_key-1, {}).get(y_key, [None, None])
            North_height = North[0] if North else None
            North_rain = North[1] if North else None
            Total_height_Norht = sum(North)

            South = x_dict.get(x_key+1, {}).get(y_key, [None, None])
            South_height = South[0] if South else None
            South_rain = South[1] if South else None
            Total_height_South = sum(South)

            West = y_dict.get(y_key-1, [None, None])
            West_height = West[0] if West else None
            West_rain = West[1] if West else None
            Total_height_West = sum(West)

            East = y_dict.get(y_key+1, [None, None])
            East_height = East[0] if East else None
            East_rain = East[1] if East else None
            Total_height_East = sum(East)

            # Nothing happens
                # All Total heights are equal to or higher than current cell;s Total height
            # Something happens
                # One or more of the cells' Total heights are lower than the current cell's Total height
print(json.dumps(x_dict, indent=4))
