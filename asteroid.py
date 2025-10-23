import pygame
import random

from constants import ASTEROID_MIN_RADIUS, NEW_ASTEROID_SPEED
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (155, 155, 155), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Destroy and return on the smallest asteroids
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create a random angle
        random_angle = random.uniform(20, 50)

        # Assign an 'a' and 'b' velocity
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # Assign a new (1 size smaller asteroid) radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create 2 new asteroids with a random offset velocity
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = a * NEW_ASTEROID_SPEED
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = b * NEW_ASTEROID_SPEED