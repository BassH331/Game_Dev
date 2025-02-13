import pygame as pg

# Initialize Pygame
pg.init()

# Set up the screen
screen = pg.display.set_mode((1600, 830))
pg.display.set_caption("2D Game with Player and Background")

# Game active state so that we can check for when the user wants to either restart the game or quit
game_active = False

# Load the background image (make sure the image is in the same folder or provide the path)
background = pg.image.load('Old forest(night).jpg').convert_alpha()  # Replace with your image file
player = pg.image.load('fire_knight/01_idle/idle_1.png').convert_alpha()
background = pg.transform.scale(background, (1600, 830))  # Scale to fit screen

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(player, (0, 0))
    # Update the display
    pg.display.flip()

# Quit Pygame
pg.quit()
