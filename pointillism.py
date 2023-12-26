import pygame
import sys

# Initialize the Pygame library
pygame.init()

# Load the user-provided image from the command line argument
user_image = pygame.image.load(sys.argv[1])

# Get the dimensions of the image
image_height = user_image.get_height()
image_width = user_image.get_width()

# Create a window with dimensions matching the image
window = pygame.display.set_mode([image_width, image_height])
window.blit(user_image, (0, 0))

exit_flag = False
click_flag = True

while not exit_flag:
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if click_flag:
                pos1 = pygame.mouse.get_pos()
                click_flag = False
            else:
                pos2 = pygame.mouse.get_pos()
                click_flag = True

            if click_flag:
                pos1x, pos2x = pos1[0], pos2[0]
                pos1y, pos2y = pos1[1], pos2[1]

                top_left_x = min(pos1x, pos2x)
                top_left_y = min(pos1y, pos2y)
                
                width = abs(pos1x - pos2x)
                height = abs(pos1y - pos2y)

                # Iterate through each pixel in the selected area
                for x in range(width + 1):
                    for y in range(height + 1):
                        # Invert the RGB values of each pixel
                        r, g, b, _ = window.get_at((x + top_left_x, y + top_left_y))
                        window.set_at((x + top_left_x, y + top_left_y), (255 - r, 255 - g, 255 - b))

    pygame.display.update()

    for event in events:
        if event.type == pygame.QUIT:
            exit_flag = True
            pygame.quit()
            quit()
