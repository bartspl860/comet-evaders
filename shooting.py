from entity import *

class Bullet(Entity):
    def __init__(self, position: Vector2, width: float, height: float, speed=5, velocity_falloff=1) -> None:
        super().__init__(position, width, height, speed, velocity_falloff)

    def launch(self, direction: Vector2) -> None:
        self.velocity = direction

class Asteroid(Bullet):
    def __init__(self, position: Vector2, width: float, height: float, speed=2, velocity_falloff=1) -> None:
        super().__init__(position, width, height, speed, velocity_falloff)