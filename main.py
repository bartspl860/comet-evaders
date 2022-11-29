import pygame
from pygame.locals import *

from player import *

pygame.init()
pygame.font.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

player = Player(Vector2(screen_width/2-24, screen_height/2-35), 48, 70, 3, 0.8)

player.set_limit(Vector2(0, screen_width-48), Vector2(0, screen_height-70))

image = pygame.image.load("sprites\spaceship.png")
player.load_sprite(image)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...
    player.update()     # Update player position

    for bullet in player.bullets:
        bullet.update()

    

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    player.draw(screen)    # Draw player on the screen
    for bullet in player.bullets:
        bullet.draw(screen)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
