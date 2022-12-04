import pygame
from pygame.locals import *
from player import *
from entity_factory import *
import globals; from globals import *

globals.initialize()

if (__name__ == "__main__"):

    pygame.init()
    # pygame.font.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    player = Player(Vector2(SCREEN_WIDTH/2-24,
                    SCREEN_HEIGHT/2-35), 48, 70, 3, 0.8)    

    # Set player movement limit
    player.set_limit(Vector2(0, SCREEN_WIDTH-48), Vector2(0, SCREEN_HEIGHT-70))

    image = pygame.image.load("sprites/spaceship.png")  # Set sprite for player
    player.load_sprite(image)  # Load sprite to player instance

    entiryFactory = EntityFactory()


    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # ...
        player.update()     # Update player position        
        entiryFactory.update()

        # Render the graphics here.
        # ...

        screen.fill("black")  # Fill the display with a solid color
        player.draw(screen)    # Draw player on the screen

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)
