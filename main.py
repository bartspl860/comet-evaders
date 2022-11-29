import pygame
from pygame.locals import *

from player import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

player = Player(Vector2(10, 10), 30, 30, 2, 0.8)
image = pygame.image.load("sprites\squareman.png")
player.load_sprite(image)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    print(player.velocity)

    # Do logical updates here.
    # ...
    player.update()

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    player.draw(screen)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
