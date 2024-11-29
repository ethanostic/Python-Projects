import json
import random
x_dict = {}
y_dict = {}

number= int(input("Number of terrain strengths: "))
# Make the X dictionary
x_length = int(input("X: "))
for i in range(1, x_length+1):
    x_dict[i] = None

# Make the Y dictionary with the height and strength values inside it.
y_length =  int(input("Y: "))
for i in range(1, y_length+1):
    y_dict[i] = h_and_strength = [i, random.randint(1, number)]

# Nest it in the X dictionary
for y in x_dict.keys():
    x_dict[y] = y_dict

print(json.dumps(x_dict, indent=4))
