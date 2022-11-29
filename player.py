import entity
from entity import *

class Player(Entity):     
    def __init__(self, position: Vector2, width: float, height: float, speed=1, velocity_falloff=0.95) -> None:
        super().__init__(position, width, height, speed, velocity_falloff)
        
    def update(self) -> None:
        super().update()
        if pygame.key.get_pressed()[pygame.K_d]: 
            self.velocity.x = self.speed
        if pygame.key.get_pressed()[pygame.K_a]: 
            self.velocity.x = -self.speed
        if pygame.key.get_pressed()[pygame.K_w]: 
            self.velocity.y = -self.speed
        if pygame.key.get_pressed()[pygame.K_s]: 
            self.velocity.y = self.speed


    