from entity import *
from shooting import *
import globals
import random

class EntityFactory:
    def __init__(self) -> None:
        self.entities = []
        self.ticks = 0
        self.spawn_delay = 100

    def update(self) -> None:
        print(self.entities)
        for entity in self.entities:
            entity.update()
        self.ticks += 1
        if(self.ticks > self.spawn_delay):
            self.ticks = 0
            self.random_asteroid_tick()

    def launch_asteroid(self, _from_: Vector2, _to_: Vector2, _at_speed_: float) -> None:
        asteroid = Asteroid(_from_, 20, 20)
        sprite = pygame.image.load("sprites/asteroida.png")
        asteroid.load_sprite(sprite)
        asteroid.speed = _at_speed_
        asteroid.launch(_to_)
        self.entities.append(asteroid)

    def random_asteroid_tick(self) -> None:
        spawn_point = Vector2(0, random.uniform(0, globals.SCREEN_WIDTH))
        destination = Vector2(0, random.uniform(0, globals.SCREEN_WIDTH))
        self.launch_asteroid(spawn_point, destination, 3)
