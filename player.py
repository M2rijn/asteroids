import pygame

from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (215, 215, 215), self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Ship movement with W A S D
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Shoot with space bar
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Shoot timer counting down back to zero
        self.shoot_timer -= dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return

        # Set the shoot timer
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        # Create the shot
        shot = Shot(self.position.x, self.position.y)
        # Set the shot velocity
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED