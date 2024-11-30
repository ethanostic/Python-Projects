import json
import random
x_dict = {}
y_dict = {}

# Make the X dictionary
x_length = int(input("X: "))
for i in range(1, x_length+1):
    x_dict[i] = None

# Make the Y dictionary and assign the height and Nest it in the X dictionary
y_length =  int(input("Y: "))
for y in x_dict.keys():
    for i in range(1, y_length+1):
        y_dict[i] = i + random.randint(0, 1)
    x_dict[y] = y_dict.copy()


print(json.dumps(x_dict, indent=4))
