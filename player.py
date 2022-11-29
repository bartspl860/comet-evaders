from entity import *
from shooting import *


class Player(Entity):
    def __init__(self, position: Vector2, width: float, height: float, speed=1, velocity_falloff=0.95) -> None:
        super().__init__(position, width, height, speed, velocity_falloff)
        self.limit_set = False
        self.bullets = []

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
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.shoot()
        if (self.limit_set):
            self.position.x = min(
                max(self.position.x, self.limit_hor.x), self.limit_hor.y)
            self.position.y = min(
                max(self.position.y, self.limit_ver.x), self.limit_ver.y)

    def set_limit(self, limit_hor: Vector2, limit_ver: Vector2) -> None:
        self.limit_set = True
        self.limit_hor = limit_hor
        self.limit_ver = limit_ver

    def shoot(self) -> None:
        position = self.position
        bullet = Bullet(Vector2(position.x + self.width /
                        2 - 5, position.y-20), 5, 15, 10)
        bullet.launch(Vector2(0, -bullet.speed))
        self.bullets.append(bullet)
