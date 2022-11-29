from pygame import Vector2

import pygame


class Entity:
    def __init__(self, position: Vector2, width: float, height: float, speed=1.0, velocity_falloff=0.95) -> None:
        self.position = position
        self.width = width
        self.height = height
        self.velocity = Vector2(0, 0)
        self.velocity_falloff = velocity_falloff
        self.speed = speed
        self.color = (255, 0, 0)
        self.sprite = None

    def update(self) -> None:
        self.position += self.velocity
        self.velocity *= self.velocity_falloff

    def draw(self, screen) -> None:
        if self.sprite == None:
            pygame.draw.rect(screen, self.color, pygame.Rect(
                self.position.x, self.position.y, self.width, self.height))
        else:
            screen.blit(self.sprite, self.position)
            if self.velocity.x == self.speed:
                self.sprite = pygame.transform.flip(self.sprite, True, False)

    def load_sprite(self, sprite) -> None:
        self.sprite = pygame.transform.scale(sprite, (self.width, self.height))

    def remove_sprite(self) -> None:
        self.sprite = None

    def change_color(self, color) -> None:
        self.color = color
