import pygame
import random
from copy import deepcopy

# Initialize dictionaries
x_dict = {}
y_dict = {}

# Create the X dictionary
x_length = int(input("X: "))  # This allows input for X size
for i in range(1, x_length + 1):
    x_dict[i] = None

# Create the Y dictionary and assign height and rain
y_length = int(input("Y: "))  # This allows input for Y size
for y in x_dict.keys():
    for i in range(1, y_length + 1):
        y_dict[i] = [i, random.randint(0, 2)]  # [height, rain]
    x_dict[y] = deepcopy(y_dict)

# Function to run the erosion
def erosion():
    global x_dict
    # create x_dict copy
    new_x_dict = deepcopy(x_dict)
    for x_key, y_dict in x_dict.items():
        for y_key, current_cell_data in y_dict.items():
            Middle = current_cell_data
            if Middle[1] > 0:
                neighbors = {
                    "North": x_dict.get(x_key - 1, {}).get(y_key),
                    "South": x_dict.get(x_key + 1, {}).get(y_key),
                    "West": y_dict.get(y_key - 1),
                    "East": y_dict.get(y_key + 1)
                }

                # Find neighbors with lower total height
                current_total = sum(Middle)
                lower_neighbors = {direction: data for direction, data in neighbors.items() if data and sum(data) < current_total}

                if lower_neighbors:
                    # Choose a random lower neighbor
                    chosen_direction = random.choice(list(lower_neighbors.keys()))
                    chosen_cell = lower_neighbors[chosen_direction]

                    # Update the current cell's rain and height
                    new_x_dict[x_key][y_key][0] -= 1
                    new_x_dict[x_key][y_key][1] -= 1

                    # Update the chosen cell's height and rain
                    if chosen_direction == "North":
                        new_x_dict[x_key - 1][y_key][0] -= 1
                        new_x_dict[x_key - 1][y_key][1] += 1 
                    elif chosen_direction == "South":
                        new_x_dict[x_key + 1][y_key][0] -= 1 
                        new_x_dict[x_key + 1][y_key][1] += 1
                    elif chosen_direction == "West":
                        new_x_dict[x_key][y_key - 1][0] -= 1
                        new_x_dict[x_key][y_key - 1][1] += 1
                    elif chosen_direction == "East":
                        new_x_dict[x_key][y_key + 1][0] -= 1
                        new_x_dict[x_key][y_key + 1][1] += 1

    # Apply the changes to x_dict
    x_dict = new_x_dict

# Function to add one layer of water to each block
def add_water():
    global x_dict
    for x_key, y_dict in x_dict.items():
        for y_key, cell_data in y_dict.items():
            cell_data[1] += 1  # Add one unit of water (rain)

# Pygame setup
pygame.init()

# Get window dimensions based on grid size
width = 600
height = 600
cell_size = min(width, height) // max(x_length, y_length)  # Dynamic cell size based on grid size

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Erosion Grid")

# Define button areas
erosion_button_rect = pygame.Rect(10, height - 60, 200, 50)  # Erosion button
water_button_rect = pygame.Rect(220, height - 60, 200, 50)  # Add water button
font = pygame.font.Font(None, 36)

def draw_grid():
    min_height = min(min([sum(cell) for cell in row.values()]) for row in x_dict.values())
    max_height = max(max([sum(cell) for cell in row.values()]) for row in x_dict.values())
    
    for x_key, y_dict in x_dict.items():
        for y_key, cell_data in y_dict.items():
            total_height = sum(cell_data)  # Combine height and rain
            # Normalize to a range of 0 to 255 for greyscale
            grayscale = int(255 * (total_height - min_height) / (max_height - min_height))
            color = (grayscale, grayscale, grayscale)
            pygame.draw.rect(window, color, pygame.Rect(y_key * cell_size, x_key * cell_size, cell_size, cell_size))

def draw_button():
    # Draw the erosion button
    pygame.draw.rect(window, (0, 200, 0), erosion_button_rect)  # Green button
    text_surface = font.render("Erode", True, (255, 255, 255))
    window.blit(text_surface, (erosion_button_rect.x + 50, erosion_button_rect.y + 10))

    # Draw the add water button
    pygame.draw.rect(window, (0, 0, 255), water_button_rect)  # Blue button
    text_surface = font.render("Add Water", True, (255, 255, 255))
    window.blit(text_surface, (water_button_rect.x + 50, water_button_rect.y + 10))

def main():
    running = True
    while running:
        window.fill((0, 0, 0))  # Fill the window with black before drawing
        draw_grid()
        draw_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if erosion_button_rect.collidepoint(event.pos):
                    erosion()  # Call the erosion function when the "Erode" button is pressed
                elif water_button_rect.collidepoint(event.pos):
                    add_water()  # Call the add water function when the "Add Water" button is pressed

        pygame.display.flip()

# Run the main loop
main()

# Quit pygame
pygame.quit()