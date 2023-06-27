import pygame
import random

# Define the screen dimensions and font size
screen_width = 640
screen_height = 480
font_size = 20

# Define the colors
black = (0, 0, 0)
green = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set the screen dimensions and font
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, font_size)

# Define the raindrops
raindrops = []
for i in range(screen_width // font_size):
    raindrops.append(-font_size)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill the screen with black
    screen.fill(black)

    # Draw the raindrops
    for i in range(len(raindrops)):
        # Generate a random letter
        letter = font.render(chr(random.randint(33, 126)), True, green)

        # Add the letter to the screen
        screen.blit(letter, (i * font_size, raindrops[i]))

        # Move the raindrop down
        raindrops[i] += font_size

        # Reset the raindrop if it goes off the screen
        if raindrops[i] > screen_height:
            raindrops[i] = -font_size

    # Update the screen
    pygame.display.update()
