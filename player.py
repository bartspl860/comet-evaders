from entity import *
from shooting import *


class Player(Entity):
    def __init__(self, position: Vector2, width: float, height: float, speed=1, velocity_falloff=0.95) -> None:
        super().__init__(position, width, height, speed, velocity_falloff)
        self.limit_set = False
        self.bullets = []
        self.shooting_delay = 50
        self.ticks = 0

    def update(self) -> None:
        super().update()
        self.ticks += 1
        if self.ticks > self.shooting_delay:
            self.ticks = 0
        if (self.limit_set):
            self.position.x = min(
                max(self.position.x, self.limit_hor.x), self.limit_hor.y)
            self.position.y = min(
                max(self.position.y, self.limit_ver.x), self.limit_ver.y)
        for bullet in self.bullets:
            bullet.update()
            if bullet.position.y + bullet.height < 0:
                self.bullets.remove(bullet)
        if pygame.key.get_pressed()[pygame.K_d]:
            self.velocity.x = self.speed
        if pygame.key.get_pressed()[pygame.K_a]:
            self.velocity.x = -self.speed
        if pygame.key.get_pressed()[pygame.K_w]:
            self.velocity.y = -self.speed
        if pygame.key.get_pressed()[pygame.K_s]:
            self.velocity.y = self.speed
        if self.ticks == 0:
            self.shoot()

    def draw(self, screen) -> None:
        super().draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def set_limit(self, limit_hor: Vector2, limit_ver: Vector2) -> None:
        self.limit_set = True
        self.limit_hor = limit_hor
        self.limit_ver = limit_ver

    def shoot(self) -> None:
        position = self.position
        bullet = Bullet(Vector2(position.x + self.width /
                        2 - 2, position.y), 5, 5, 10)
        bullet.launch(Vector2(0, -bullet.speed))
        self.bullets.append(bullet)

    def set_shooting_delay(self, delay: int) -> None:
        self.shooting_delay = delay
