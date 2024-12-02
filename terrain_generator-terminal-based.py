import json
import random

# Initialize dictionaries
x_dict = {}
y_dict = {}

# Create the X dictionary
x_length = int(input("X: "))
for i in range(1, x_length + 1):
    x_dict[i] = None

# Create the Y dictionary and assign height and rain
y_length = int(input("Y: "))
for y in x_dict.keys():
    for i in range(1, y_length + 1):
        y_dict[i] = [i + random.randint(0, 1), 1]
    x_dict[y] = y_dict.copy()

def erosion():
    for x_key, y_dict in x_dict.items():
        for y_key, current_cell_data in y_dict.items():

            # Get current cell and neighbors
            Middle = current_cell_data
            North = x_dict.get(x_key - 1, {}).get(y_key)
            South = x_dict.get(x_key + 1, {}).get(y_key)
            West = y_dict.get(y_key - 1)
            East = y_dict.get(y_key + 1)
            
            # Create a dictionary for these cells
            neighbors = {
                "North": North,
                "South": South,
                "West": West,
                "East": East
            }
            
            # Calculate total height for valid neighbors
            directions_height = {}
            for direction, neighbor in neighbors.items():
                if neighbor:
                    directions_height[direction] = sum(neighbor)
            
            # Find neighbors with lower total height
            current_total = sum(Middle)
            possible_directions = {}
            for direction, height in directions_height.items():
                if height < current_total:
                    possible_directions[direction] = height

            # Randomly choose a direction and update values. Only allow erosion if there is a lower cell
            if possible_directions:
                final_direction = random.choice(list(possible_directions.keys()))
                
                # Update current cell
                if Middle[0] > 0:
                    Middle[0] -= 1
                if Middle[1] > 0:
                    Middle[1] -= 1
                
                # Update chosen neighbor cell
                if final_direction == "North":
                    x_dict[x_key - 1][y_key][0] += 1
                    x_dict[x_key - 1][y_key][1] += 1
                elif final_direction == "South":
                    x_dict[x_key + 1][y_key][0] += 1
                    x_dict[x_key + 1][y_key][1] += 1
                elif final_direction == "West":
                    y_dict[y_key - 1][0] += 1
                    y_dict[y_key - 1][1] += 1
                elif final_direction == "East":
                    y_dict[y_key + 1][0] += 1
                    y_dict[y_key + 1][1] += 1

erosion()
print(json.dumps(x_dict, indent=4))