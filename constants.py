# Screen/game sizing
screen_width = 800
screen_height = 700
grid_area_width = 300
grid_area_height = 600

# How many cells per row and column
grid_size = 10, 20  # Meaning 10 x 20 grid

# how big are the cells inside
cell_width = grid_area_width / grid_size[0]
cell_height = grid_area_height / grid_size[1]

# Padding offsets from screen to grid area
screen_padding_x = (screen_width - grid_area_width) // 2
screen_padding_y = screen_height - grid_area_height

border_color = (128, 128, 128)  # Gray

# Levels
levels = [0.35, 0.33, 0.30, 0.27, 0.24, 0.20, 0.16, 0.14, 0.12, 0.10]
